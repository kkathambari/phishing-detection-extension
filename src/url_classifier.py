import joblib
from feature_extraction import extract_features

def classify_url(url):
    """Classify the URL using the trained model."""
    # Load the pre-trained model (now from the 'models' directory)
    model = joblib.load('models/random_forest_model.pkl')
    
    # Extract features
    features = extract_features(url)
    
    # Ensure that features align with the model’s expected input
    feature_list = list(features.values())  # Convert features to a list

    # Make prediction
    prediction = model.predict([feature_list])
    
    # Return classification result
    return 'Malicious' if prediction[0] == 1 else 'Benign'