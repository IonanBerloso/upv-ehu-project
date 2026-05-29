const CACHE = 'upv-study-hub-v17';

const PRECACHE = [
  '/upv-ehu-project/',
  '/upv-ehu-project/index.html',
  '/upv-ehu-project/shared/ehulab.css',
  '/upv-ehu-project/shared/print.css',
  '/upv-ehu-project/fluidos/teoria.html',
  '/upv-ehu-project/fluidos/examenes.html',
  '/upv-ehu-project/fluidos/examenes/mayo2020.html',
  '/upv-ehu-project/fluidos/examenes/mayo2021.html',
  '/upv-ehu-project/fluidos/examenes/mayo2024.html',
  '/upv-ehu-project/fluidos/examenes/mayo2025.html',
  '/upv-ehu-project/fluidos/examenes/abril2021.html',
  '/upv-ehu-project/fluidos/examenes/junio2020.html',
  '/upv-ehu-project/fluidos/examenes/junio2020ef.html',
  '/upv-ehu-project/fluidos/examenes/junio2021.html',
  '/upv-ehu-project/fluidos/examenes/junio2021ef.html',
  '/upv-ehu-project/fluidos/examenes/junio2022.html',
  '/upv-ehu-project/fluidos/examenes/junio2022ef.html',
  '/upv-ehu-project/fluidos/examenes/junio2023.html',
  '/upv-ehu-project/fluidos/examenes/junio2023ef.html',
  '/upv-ehu-project/fluidos/examenes/junio2024ef.html',
  '/upv-ehu-project/fluidos/examenes/junio2025ef.html',
  // Mecánica retirada del precache (asignatura oculta y retirada del índice)
  'https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css',
  'https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js',
  'https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js'
];

// Instalar y cachear recursos.
// Precache tolerante a fallos: cada recurso se cachea por separado, de modo que
// un único 404 no rechaza toda la instalación (a diferencia de cache.addAll, que es atómico).
self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE)
      .then(c => Promise.allSettled(PRECACHE.map(u => c.add(u))))
      .then(() => self.skipWaiting())
  );
});

// Limpiar caches viejas
self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

// Cache-first para recursos propios, network-first para externos
// EXCLUSIÓN: los PDFs (carpeta /pdf/) no se cachean para no inflar la PWA (~60 MB).
self.addEventListener('fetch', e => {
  const url = new URL(e.request.url);

  // No cachear PDFs ni binarios pesados
  if (url.pathname.includes('/pdf/') && url.pathname.endsWith('.pdf')) {
    e.respondWith(fetch(e.request).catch(() => new Response('', {status: 503})));
    return;
  }

  if (url.origin === location.origin) {
    e.respondWith(
      caches.match(e.request).then(cached =>
        cached || fetch(e.request).then(res => {
          // Solo cachear respuestas correctas (evita "pegar" 404/500 en cache-first).
          if (res && res.ok && res.status === 200) {
            const clone = res.clone();
            caches.open(CACHE).then(c => c.put(e.request, clone));
          }
          return res;
        })
      )
    );
  } else {
    e.respondWith(
      fetch(e.request).catch(() => caches.match(e.request))
    );
  }
});
