const output = document.getElementById('output');
const refreshBtn = document.getElementById('refresh');
const copyBtn = document.getElementById('copy');

// Refresh to show only the latest stream URL
refreshBtn.addEventListener('click', () => {
  chrome.storage.local.get('capturedUrls', (data) => {
    const urls = data.capturedUrls || [];
    output.value = urls.length ? urls[urls.length - 1] : '';
  });
});

// Copy the current stream URL to clipboard
copyBtn.addEventListener('click', () => {
  output.select();
  document.execCommand('copy');
});

// Initial state
output.value = '';
