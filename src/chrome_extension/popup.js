document.getElementById("check-url-btn").addEventListener("click", function () {
    const url = document.getElementById("url-input").value;

    if (url) {
        chrome.runtime.sendMessage(
            { action: "classifyUrl", url: url },
            function (response) {
                const result = response.result;
                const body = document.body;
                const resultText = document.getElementById("result-text");

                if (!resultText) {
                    // Create the result text element if not already present
                    const newResultText = document.createElement("div");
                    newResultText.id = "result-text";
                    body.appendChild(newResultText);
                }

                const resultTextElement = document.getElementById("result-text");

                if (result === "Malicious") {
                    resultTextElement.textContent = "The URL is Malicious!";
                    resultTextElement.style.color = "#ff0000";
                    body.style.background = "linear-gradient(145deg, #330000, #550000)";
                    body.style.boxShadow = "inset 0 0 50px #ff0000";
                } else if (result === "Benign") {
                    resultTextElement.textContent = "The URL is Benign.";
                    resultTextElement.style.color = "#00ff00";
                    body.style.background = "linear-gradient(145deg, #002200, #004400)";
                    body.style.boxShadow = "inset 0 0 50px #00ff00";
                } else {
                    resultTextElement.textContent = "Error classifying URL.";
                    resultTextElement.style.color = "#ff8800";
                    body.style.background = "linear-gradient(145deg, #121212, #1b1b1b)";
                    body.style.boxShadow = "inset 0 0 50px #ff8800";
                }
            }
        );
    } else {
        alert("Please enter a URL.");
    }
});
