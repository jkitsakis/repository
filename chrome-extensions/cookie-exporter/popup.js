document.addEventListener("DOMContentLoaded", async () => {
  const output = document.getElementById("cookieOutput");
  const sentOutput = document.getElementById("sentCookieOutput");
  const copyBtn = document.getElementById("copyButton");
  const downloadBtn = document.getElementById("downloadButton");
  const refreshBtn = document.getElementById("refreshButton");
  const status = document.getElementById("status");

  refreshBtn.addEventListener("click", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      const tabId = tabs[0].id;
      chrome.tabs.reload(tabId, {}, () => {
        setTimeout(() => {
          chrome.scripting.executeScript({
            target: { tabId: tabId },
            files: ["inject.js"]
          });
          setTimeout(() => {
            loadSentCookies();
          }, 1500);
        }, 1000);
      });
    });
  });

  copyBtn.addEventListener("click", () => {
    navigator.clipboard.writeText(sentOutput.value).then(() => {
      copyBtn.textContent = "Copied!";
      setTimeout(() => (copyBtn.textContent = "Copy to Clipboard"), 1500);
    });
  });

  downloadBtn.addEventListener("click", () => {
    const blob = new Blob([sentOutput.value], { type: "text/plain" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "latest_cookie.txt";
    a.click();
    URL.revokeObjectURL(url);
  });



  function loadSentCookies() {
    chrome.storage.local.get("lastSentCookies", (data) => {
      sentOutput.value = data.lastSentCookies || "[No request yet]";
    });
  }

  // Initial load
  loadSentCookies();
});
