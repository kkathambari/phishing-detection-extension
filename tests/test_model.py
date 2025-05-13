import os
import joblib
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
import time

def test_model():
    """
    Test the trained model using a separate dataset.
    """
    start_time = time.time()  # Start the timer
    # Paths to the saved model and feature columns
    model_path = 'models/random_forest_model.pkl'
    feature_columns_path = 'models/feature_columns.pkl'
    test_data_path = 'datasets/test_dataset.csv'  # Path to the test dataset (CSV file)

    # Check if the required files exist
    if not os.path.exists(model_path):
        print(f"Error: Model file {model_path} not found. Please ensure the model is trained and saved.")
        return

    if not os.path.exists(feature_columns_path):
        print(f"Error: Feature columns file {feature_columns_path} not found. Please ensure the feature columns are saved.")
        return

    if not os.path.exists(test_data_path):
        print(f"Error: Test data file {test_data_path} not found. Please ensure the test data is available.")
        return

    # Load the trained model and feature columns
    model = joblib.load(model_path)
    feature_columns = joblib.load(feature_columns_path)

    # Load the test dataset
    test_data = pd.read_csv(test_data_path)

    # Strip any extra spaces in column names to avoid mismatches
    test_data.columns = test_data.columns.str.strip()

    # Debugging: Check if 'phishing' column is present
    print("Columns in test data:", test_data.columns.tolist())

    # Check if the test dataset contains the target label 'phishing'
    if 'phishing' not in test_data.columns:
        print("Error: Test data must contain the target label 'phishing'.")
        return

    # Ensure the test dataset includes all required feature columns
    missing_columns = [col for col in feature_columns if col not in test_data.columns]
    if missing_columns:
        print(f"Error: The following required feature columns are missing from the test data: {missing_columns}")
        return

    # Ensure the test dataset includes only the required feature columns
    # Drop any extra columns not used during training
    test_data = test_data[feature_columns + ['phishing']]

    # Split the features (X) and target (y) in the test dataset
    X_test = test_data.drop('phishing', axis=1)  # Drop the target column
    y_test = test_data['phishing']  # Extract the target column

    # Predict using the trained model
    y_pred = model.predict(X_test)

    # Evaluate predictions
    print("Classification Report:\n", classification_report(y_test, y_pred, zero_division=0))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

    end_time = time.time()  # End the timer
    execution_time = end_time - start_time
    print(f"Total time taken for model training: {execution_time:.2f} seconds")


if __name__ == "__main__":
    test_model()
