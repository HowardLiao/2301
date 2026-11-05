// v2: network-first so updates reach visitors immediately; old caches are cleared.
const CACHE_NAME = 'liteon-2301-v2';
self.addEventListener('install', e => { self.skipWaiting(); });
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  e.respondWith(fetch(e.request).then(res => {
    const copy = res.clone(); caches.open(CACHE_NAME).then(c => c.put(e.request, copy)).catch(() => {}); return res;
  }).catch(() => caches.match(e.request).then(r => r || caches.match('./index.html'))));
});
