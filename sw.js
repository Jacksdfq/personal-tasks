var CACHE_NAME = 'personal-tasks-v5';
var BASE = self.location.pathname.replace(/\/[^/]*$/, '');

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME).then(function(cache) {
      return cache.addAll([BASE + '/', BASE + '/index.html', BASE + '/manifest.json']);
    }).then(function() { return self.skipWaiting(); })
  );
});

self.addEventListener('activate', function(event) {
  event.waitUntil(
    caches.keys().then(function(cacheNames) {
      return Promise.all(
        cacheNames.map(function(cacheName) {
          if (cacheName !== CACHE_NAME) return caches.delete(cacheName);
        })
      );
    }).then(function() { return self.clients.claim(); })
  );
});

self.addEventListener('fetch', function(event) {
  if (!event.request.url.startsWith(self.location.origin)) return;
  event.respondWith(
    fetch(event.request).then(function(response) {
      if (!response || response.status !== 200 || response.type !== 'basic') return response;
      var toCache = response.clone();
      caches.open(CACHE_NAME).then(function(cache) { cache.put(event.request, toCache); });
      return response;
    }).catch(function() {
      return caches.match(event.request);
    })
  );
});

self.addEventListener('notificationclick', function(event) {
  event.notification.close();
  event.waitUntil(
    clients.matchAll({ type: 'window' }).then(function(clientList) {
      for (var i = 0; i < clientList.length; i++) {
        var client = clientList[i];
        if (client.url && 'focus' in client) return client.focus();
      }
      if (clients.openWindow) return clients.openWindow(BASE + '/');
    })
  );
});

self.addEventListener('periodicsync', function(event) {
  if (event.tag === 'check-reminders') {
    event.waitUntil(
      clients.matchAll().then(function(clients) {
        clients.forEach(function(client) { client.postMessage({ type: 'check-reminders' }); });
      })
    );
  }
});
