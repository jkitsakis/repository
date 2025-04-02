(async () => {
  console.log("[EXT] Injected script running...");

  // Use a relative URL to ensure same-origin request (avoids CORS)
  const path = window.location.pathname !== "/" ? "/" : "/favicon.ico"; // fallback to a small request
  try {
    const res = await fetch(path, {
      method: "GET",
      credentials: "include",
      cache: "no-store",
    });
    console.log("[EXT] Triggered fetch to:", path);
  } catch (err) {
    console.error("[EXT] Failed to trigger fetch:", err);
  }
})();
