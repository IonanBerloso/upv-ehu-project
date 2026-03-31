const CACHE = 'upv-study-hub-v9';

const PRECACHE = [
  '/upv-ehu-project/',
  '/upv-ehu-project/index.html',
  '/upv-ehu-project/fluidos/teoria.html',
  '/upv-ehu-project/fluidos/examenes.html',
  '/upv-ehu-project/fluidos/examenes/mayo2020.html',
  '/upv-ehu-project/fluidos/examenes/abril2021.html',
  '/upv-ehu-project/fluidos/examenes/junio2020.html',
  '/upv-ehu-project/fluidos/examenes/junio2020ef.html',
  '/upv-ehu-project/fluidos/examenes/junio2021ef.html',
  '/upv-ehu-project/fluidos/examenes/junio2022.html',
  '/upv-ehu-project/fluidos/examenes/junio2022ef.html',
  '/upv-ehu-project/fluidos/examenes/junio2023.html',
  '/upv-ehu-project/mecanica/teoria.html',
  '/upv-ehu-project/mecanica/ejercicios.html',
  'https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css',
  'https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js',
  'https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js'
];

// Instalar y cachear recursos
self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE).then(c => c.addAll(PRECACHE)).then(() => self.skipWaiting())
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
self.addEventListener('fetch', e => {
  const url = new URL(e.request.url);
  if (url.origin === location.origin) {
    e.respondWith(
      caches.match(e.request).then(cached =>
        cached || fetch(e.request).then(res => {
          const clone = res.clone();
          caches.open(CACHE).then(c => c.put(e.request, clone));
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
