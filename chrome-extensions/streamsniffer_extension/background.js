chrome.webRequest.onBeforeRequest.addListener(
  function (details) {
    const url = details.url;
    if (url.match(/\.(m3u8|mp4|mpd|flv)(\?.*)?$/)) {
      chrome.storage.local.set({ capturedUrls: [url] });
    }
  },
  { urls: ["<all_urls>"] },
  []
);