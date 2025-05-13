import re
from sklearn.metrics import classification_report, accuracy_score

def clean_url(url):
    """
    Cleans the URL by removing unnecessary parameters.
    """
    # Remove fragments and query parameters
    clean_url = re.sub(r'\?.*|#.*', '', url)
    return clean_url

def print_evaluation_metrics(y_true, y_pred):
    """
    Prints evaluation metrics for the model.
    """
    print("Classification Report:")
    print(classification_report(y_true, y_pred))
    print(f"Accuracy: {accuracy_score(y_true, y_pred):.2f}")

def save_predictions_to_file(predictions, file_path):
    """
    Saves predictions to a file for analysis.
    """
    with open(file_path, "w") as file:
        for prediction in predictions:
            file.write(f"{prediction}\n")
    print(f"Predictions saved to {file_path}")
