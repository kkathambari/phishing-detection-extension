from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import joblib
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
import pandas as pd
import time


def train_model():
    # Start the timer
    start_time = time.time()  

    # Load the dataset
    data = pd.read_csv('datasets/phishing_dataset.csv')

    # Feature columns 
    feature_columns = [
        'qty_dot_url', 'qty_hyphen_url', 'qty_underline_url', 'qty_slash_url', 'qty_questionmark_url', 
        'qty_equal_url', 'qty_at_url', 'qty_and_url', 'qty_exclamation_url', 'qty_space_url', 
        'qty_tilde_url', 'qty_comma_url', 'qty_plus_url', 'qty_asterisk_url', 'qty_hashtag_url', 
        'qty_dollar_url', 'qty_percent_url', 'qty_tld_url', 'length_url', 'qty_dot_domain', 
        'qty_hyphen_domain', 'qty_underline_domain', 'qty_slash_domain', 'qty_questionmark_domain', 
        'qty_equal_domain', 'qty_at_domain', 'qty_and_domain', 'qty_exclamation_domain', 
        'qty_space_domain', 'qty_tilde_domain', 'qty_comma_domain', 'qty_plus_domain', 
        'qty_asterisk_domain', 'qty_hashtag_domain', 'qty_dollar_domain', 'qty_percent_domain', 
        'qty_vowels_domain', 'domain_length', 'domain_in_ip', 'server_client_domain', 
        'qty_dot_directory', 'qty_hyphen_directory', 'qty_underline_directory', 'qty_slash_directory', 
        'qty_questionmark_directory', 'qty_equal_directory', 'qty_at_directory', 'qty_and_directory', 
        'qty_exclamation_directory', 'qty_space_directory', 'qty_tilde_directory', 'qty_comma_directory', 
        'qty_plus_directory', 'qty_asterisk_directory', 'qty_hashtag_directory', 'qty_dollar_directory', 
        'qty_percent_directory', 'directory_length', 'qty_dot_file', 'qty_hyphen_file', 
        'qty_underline_file', 'qty_slash_file', 'qty_questionmark_file', 'qty_equal_file', 
        'qty_at_file', 'qty_and_file', 'qty_exclamation_file', 'qty_space_file', 'qty_tilde_file', 
        'qty_comma_file', 'qty_plus_file', 'qty_asterisk_file', 'qty_hashtag_file', 'qty_dollar_file', 
        'qty_percent_file', 'file_length', 'qty_dot_params', 'qty_hyphen_params', 'qty_underline_params', 
        'qty_slash_params', 'qty_questionmark_params', 'qty_equal_params', 'qty_at_params', 
        'qty_and_params', 'qty_exclamation_params', 'qty_space_params', 'qty_tilde_params', 
        'qty_comma_params', 'qty_plus_params', 'qty_asterisk_params', 'qty_hashtag_params', 
        'qty_dollar_params', 'qty_percent_params', 'params_length', 'tld_present_params', 
        'qty_params', 'email_in_url', 'time_response', 'domain_spf', 'asn_ip', 
        'time_domain_activation', 'time_domain_expiration', 'qty_ip_resolved', 'qty_nameservers', 
        'qty_mx_servers', 'ttl_hostname', 'tls_ssl_certificate', 'qty_redirects', 
        'url_google_index', 'domain_google_index', 'url_shortened'
    ]

    target_column = 'phishing'

    # Extract features and target
    X = data[feature_columns]
    y = data[target_column]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Resampling: Using SMOTE to balance the classes
    smote = SMOTE(sampling_strategy='auto', random_state=42)
    X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

    # Hyperparameter tuning with GridSearchCV
    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [None, 10],
        'min_samples_split': [2, 5],
        'min_samples_leaf': [1, 2],
        'class_weight': ['balanced', None]
    }

    # Initialize Random Forest
    rf = RandomForestClassifier(random_state=42)

    # GridSearchCV
    grid_search = GridSearchCV(rf, param_grid, cv=5)
    grid_search.fit(X_train_resampled, y_train_resampled)

    # Best model from GridSearchCV
    best_model = grid_search.best_estimator_

    # Model Evaluation
    y_pred_train = best_model.predict(X_train)
    y_pred_test = best_model.predict(X_test)

    print("Training Classification Report:\n", classification_report(y_train, y_pred_train))
    print("Test Classification Report:\n", classification_report(y_test, y_pred_test))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_test))

    # Save the model and feature columns
    joblib.dump(best_model, 'models/random_forest_model.pkl')
    joblib.dump(feature_columns, 'models/feature_columns.pkl')

    end_time = time.time()  # End the timer
    execution_time = end_time - start_time
    print(f"Total time taken for model training: {execution_time:.2f} seconds")

if __name__ == "__main__":
    train_model()