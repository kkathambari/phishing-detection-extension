chrome.runtime.onInstalled.addListener(() => {
  console.log("Malicious URL Detector extension installed.");
});

// Listen for requests to classify a URL
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === "classifyUrl") {
    const url = message.url;
    
    // Call the Flask API for classification
    fetch(`http://localhost:5000/classify?url=${encodeURIComponent(url)}`)
      .then(response => response.json())
      .then(data => {
        sendResponse({ result: data.result });
      })
      .catch(error => {
        sendResponse({ result: "Error" });
        console.error("Error classifying URL:", error);
      });
    
    // Keep the message channel open until the response is received
    return true;
  }
});
