"""SEO/PWA: completa el <head> de las páginas servidas y genera artefactos de raíz.

Por cada HTML servido (excluye obsidian/, tools/, .git) añade, SOLO si falta:
  - <meta viewport>, <meta description> (derivada del <title>)
  - <link canonical>, <link icon> y <link apple-touch-icon>
  - Open Graph + Twitter Card
  - <meta robots noindex> en mecanica/** y prototipo.html (retirados del índice)
Además genera sitemap.xml (sin mecanica/ ni noindex), robots.txt y 404.html.
Idempotente: re-ejecutar no duplica nada.
"""
import os
import re
import html as _html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://ionanberloso.github.io/upv-ehu-project/'
ICON192 = '/upv-ehu-project/icons/icon-192.png'
OG_IMG = BASE + 'icons/icon-512.png'
SKIP_DIRS = {'obsidian', '.git', 'tools', 'icons'}
SERVE_EXCLUDE = ('obsidian', '.git', 'tools')

def is_noindex(rel):
    rel = rel.replace('\\', '/')
    return rel.startswith('mecanica/') or rel in ('prototipo.html', '404.html')

def canonical_for(rel):
    rel = rel.replace('\\', '/')
    if rel == 'index.html':
        return BASE
    if rel.endswith('/index.html'):
        return BASE + rel[:-len('index.html')]
    return BASE + rel

def clean_desc(title):
    t = re.sub(r'\s+', ' ', title).strip()
    t = t.replace('·', '-')
    if len(t) > 158:
        t = t[:155].rstrip() + '...'
    return t

served = []           # (rel, path)
for dirpath, dirs, files in os.walk(ROOT):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    for fn in files:
        if not fn.endswith('.html'):
            continue
        p = os.path.join(dirpath, fn)
        rel = os.path.relpath(p, ROOT).replace('\\', '/')
        served.append((rel, p))

patched = 0
sitemap_urls = []
for rel, p in served:
    s = open(p, encoding='utf-8').read()
    m = re.search(r'</head>', s, re.IGNORECASE)
    if not m:
        continue
    head = s[:m.start()]
    tm = re.search(r'<title>(.*?)</title>', s, re.S | re.I)
    title = _html.unescape(re.sub(r'<[^>]+>', '', tm.group(1)).strip()) if tm else 'UPV/EHU — Apuntes de Ingeniería'
    desc = clean_desc(title)
    canon = canonical_for(rel)
    noindex = is_noindex(rel)

    add = []
    def have(token):
        return token.lower() in head.lower()
    if not have('name="viewport"'):
        add.append('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    if noindex and not have('name="robots"'):
        add.append('<meta name="robots" content="noindex, follow">')
    if not have('name="description"'):
        add.append('<meta name="description" content="%s">' % _html.escape(desc, quote=True))
    if not have('rel="canonical"'):
        add.append('<link rel="canonical" href="%s">' % canon)
    if not have('rel="icon"'):
        add.append('<link rel="icon" href="%s">' % ICON192)
    if not have('apple-touch-icon'):
        add.append('<link rel="apple-touch-icon" href="%s">' % ICON192)
    if not have('og:title'):
        add += [
            '<meta property="og:type" content="website">',
            '<meta property="og:title" content="%s">' % _html.escape(title, quote=True),
            '<meta property="og:description" content="%s">' % _html.escape(desc, quote=True),
            '<meta property="og:url" content="%s">' % canon,
            '<meta property="og:image" content="%s">' % OG_IMG,
            '<meta name="twitter:card" content="summary">',
        ]
    if add:
        block = '\n' + '\n'.join('  ' + a for a in add) + '\n'
        s = s[:m.start()] + block + s[m.start():]
        open(p, 'w', encoding='utf-8').write(s)
        patched += 1
    if not noindex:
        sitemap_urls.append(canon)

# sitemap.xml
sitemap_urls = sorted(set(sitemap_urls))
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in sitemap_urls:
    sm.append('  <url><loc>%s</loc></url>' % u)
sm.append('</urlset>\n')
open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8').write('\n'.join(sm))

# robots.txt
robots = ('User-agent: *\n'
          'Allow: /\n'
          'Disallow: /upv-ehu-project/mecanica/\n'
          'Sitemap: %ssitemap.xml\n' % BASE)
open(os.path.join(ROOT, 'robots.txt'), 'w', encoding='utf-8').write(robots)

print('Paginas con <head> completado:', patched)
print('URLs en sitemap (sin mecanica/noindex):', len(sitemap_urls))
