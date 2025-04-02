chrome.webRequest.onBeforeSendHeaders.addListener(
  (details) => {
    const cookieHeader = details.requestHeaders.find(
      (h) => h.name.toLowerCase() === "cookie"
    );
    if (cookieHeader) {
      chrome.storage.local.set({ lastSentCookies: cookieHeader.value });
      console.log("✅ Captured Cookie header:", cookieHeader.value);
    }
  },
  { urls: ["<all_urls>"] },
  ["requestHeaders", "extraHeaders"] // <-- Add "extraHeaders"
);
