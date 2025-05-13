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
# 🛡️ Phishing Detection System using Machine Learning

A comprehensive phishing URL detection system that combines a trained machine learning model, Flask-based API, Chrome browser extension, and detailed analysis tools to identify and block phishing websites with high accuracy.

---

## 📌 Features

- 🔍 **URL Feature Extraction** — Uses handcrafted features for phishing detection
- 🧠 **Random Forest Classifier** — Trained on a balanced dataset with SMOTE
- 🌐 **Flask REST API** — Exposes the model via HTTP endpoints
- 🧩 **Chrome Extension** — Classifies URLs directly within the browser
- 🧪 **Test Suite** — Unit tests for model, API, and feature extraction logic
- 📈 **95% Accuracy** — Achieved through rigorous training and evaluation

---

## 🗂️ Project Structure

```bash
phishing-detection-extension/
├── app.py                         # Flask API
├── models/
│   ├── random_forest_model.pkl    # Trained ML model
│   └── feature_columns.pkl        # List of selected features
├── datasets/
│   ├── phishing_dataset.csv
│   └── test_dataset.csv
├── src/
│   ├── feature_extraction.py      # URL feature extraction logic
│   ├── model_training.py          # Training script
│   ├── url_classifier.py          # Model loading and prediction
│   ├── utils/
│   │   └── helper_functions.py
│   └── chrome_extension/
│       ├── manifest.json
│       ├── background.js
│       ├── popup.html
│       ├── popup.js
│       └── styles.css
├── tests/
│   ├── test_model.py
│   ├── test_api.py
│   └── test_feature_extraction.py
├── analysis/
│   └── exploratory_analysis.py
├── requirements.txt
├── .gitignore
└── README.md
