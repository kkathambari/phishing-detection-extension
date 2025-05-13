from flask import Flask, request, jsonify
import joblib
from src.feature_extraction import extract_features

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained model and feature columns
MODEL_PATH = 'models/random_forest_model.pkl'
FEATURE_COLUMNS_PATH = 'models/feature_columns.pkl'
model = joblib.load(MODEL_PATH)
feature_columns = joblib.load(FEATURE_COLUMNS_PATH)

@app.route('/classify', methods=['GET'])
def classify_url():
    """
    Endpoint to classify a URL as 'Malicious' or 'Benign'.
    """
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "No URL provided."}), 400

    # Extract features
    try:
        features = extract_features(url)

        # Align features with the model's feature columns
        features = features[feature_columns]
    except Exception as e:
        return jsonify({"error": f"Error extracting or aligning features: {str(e)}"}), 500

    # Predict using the model
    try:
        prediction = model.predict(features)[0]
        result = "Malicious" if prediction == 1 else "Benign"
        return jsonify({"url": url, "result": result})
    except Exception as e:
        return jsonify({"error": f"Error during prediction: {str(e)}"}), 500

@app.route('/', methods=['GET'])
def home():
    """
    Basic endpoint to test the server.
    """
    return jsonify({"message": "Malicious URL Detection Server is running."})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)