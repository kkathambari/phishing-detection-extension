# Malicious URL Detector

A Google Chrome extension powered by machine learning to detect malicious URLs.

## Features

- Real-time URL classification.
- Integration with a Chrome extension for user interaction.
- Machine learning model trained on the UCI Phishing Websites Dataset.

## How to Run

1. Install dependencies: `pip install -r requirements.txt`
2. Train the model: `python src/model_training.py`
3. Start the server: `python src/app.py` (To be implemented for serving the model)
4. Load the Chrome extension:
   - Go to `chrome://extensions/`
   - Enable "Developer mode."
   - Click "Load unpacked" and select the `src/chrome_extension` folder.
5. Enter a URL in the extension popup to classify.
