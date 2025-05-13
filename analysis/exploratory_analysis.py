import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from collections import Counter
import re

# Load dataset
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Basic Data Overview
def data_overview(df):
    print("Column names in the dataset:")
    print(df.columns)

    print("\nFirst 5 records in the dataset:")
    print(df.head())

    print("\nDataframe info:")
    print(df.info())

    print("\nDataframe description:")
    print(df.describe())

    print("\nMissing values in the dataset:")
    print(df.isnull().sum())

# Data Visualization
def plot_data_distribution(df):
    # Plot distribution of labels (phishing vs legitimate)
    plt.figure(figsize=(8, 6))
    sns.countplot(x='phishing', data=df)
    plt.title('Distribution of Phishing vs Legitimate URLs')
    plt.show()

def plot_feature_distribution(df):
    # Visualizing distributions of some URL-related features
    features_to_plot = ['qty_dot_url', 'qty_hyphen_url', 'qty_underline_url', 'qty_slash_url', 
                        'qty_questionmark_url', 'qty_equal_url', 'qty_at_url', 'qty_and_url', 'qty_exclamation_url', 'qty_space_url']

    for feature in features_to_plot:
        plt.figure(figsize=(8, 6))
        sns.histplot(df[feature], kde=True, color='blue')
        plt.title(f'Distribution of {feature}')
        plt.show()

# Feature Importance
def plot_feature_importance(df):
    features = ['qty_dot_url', 'qty_hyphen_url', 'qty_underline_url', 'qty_slash_url', 
                'qty_questionmark_url', 'qty_equal_url', 'qty_at_url', 'qty_and_url', 'qty_exclamation_url', 'qty_space_url']
    X = df[features]
    y = df['phishing']

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)

    feature_importance = model.feature_importances_
    sorted_idx = np.argsort(feature_importance)[::-1]

    plt.figure(figsize=(10, 6))
    plt.barh(np.array(features)[sorted_idx], feature_importance[sorted_idx])
    plt.title('Feature Importance from Random Forest Model')
    plt.xlabel('Importance')
    plt.show()

# Outliers Detection
def plot_outliers(df):
    features_to_plot = ['qty_dot_url', 'qty_hyphen_url', 'qty_underline_url', 'qty_slash_url', 
                        'qty_questionmark_url', 'qty_equal_url', 'qty_at_url', 'qty_and_url', 'qty_exclamation_url', 'qty_space_url']
    
    for feature in features_to_plot:
        plt.figure(figsize=(8, 6))
        sns.boxplot(x=df[feature])
        plt.title(f'Boxplot for {feature}')
        plt.show()

# Feature Distribution by Class (Phishing vs Legitimate)
def plot_feature_distribution_by_class(df):
    features_to_plot = ['qty_dot_url', 'qty_hyphen_url', 'qty_underline_url', 'qty_slash_url', 
                        'qty_questionmark_url', 'qty_equal_url', 'qty_at_url', 'qty_and_url', 'qty_exclamation_url', 'qty_space_url']
    
    for feature in features_to_plot:
        plt.figure(figsize=(8, 6))
        sns.boxplot(x='phishing', y=feature, data=df)
        plt.title(f'{feature} Distribution by Phishing Class')
        plt.show()

# Pairwise Feature Relationships
def plot_pairwise_features(df):
    features_to_plot = ['qty_dot_url', 'qty_hyphen_url', 'qty_underline_url', 'qty_slash_url', 
                        'qty_questionmark_url', 'qty_equal_url', 'qty_at_url', 'qty_and_url', 'qty_exclamation_url', 'qty_space_url']
    
    sns.pairplot(df[features_to_plot + ['phishing']], hue='phishing')
    plt.title('Pairwise Relationships Between Features by Class')
    plt.show()

# Correlation Between Features
def plot_feature_correlation(df):
    url_features = ['qty_dot_url', 'qty_hyphen_url', 'qty_underline_url', 'qty_slash_url', 
                    'qty_questionmark_url', 'qty_equal_url', 'qty_at_url', 'qty_and_url', 'qty_exclamation_url', 'qty_space_url']
    
    corr = df[url_features].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Between URL Features')
    plt.show()

# Correlation with Target Variable
def plot_correlation_with_target(df):
    corr_target = df.corr()['phishing'].sort_values(ascending=False)
    plt.figure(figsize=(8, 6))
    sns.barplot(x=corr_target.index, y=corr_target.values)
    plt.title('Correlation of Features with Phishing Target')
    plt.xticks(rotation=90)
    plt.show()

# Class Balance Analysis
def plot_class_balance(df):
    plt.figure(figsize=(8, 6))
    sns.countplot(x='phishing', data=df)
    plt.title('Class Balance: Phishing vs Legitimate URLs')
    plt.show()

    print("\nClass distribution:")
    print(df['phishing'].value_counts())

# Missing Values Heatmap
def plot_missing_values(df):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
    plt.title('Missing Values Heatmap')
    plt.show()

# Textual Feature Analysis (URL Length & Common Words)
def plot_url_length_distribution(df):
    df['url_length'] = df['url'].apply(len)
    plt.figure(figsize=(8, 6))
    sns.histplot(df['url_length'], kde=True)
    plt.title('URL Length Distribution')
    plt.show()

def plot_common_words_in_url(df):
    df['url_words'] = df['url'].apply(lambda x: re.findall(r'\w+', x.lower()))
    all_words = sum(df['url_words'], [])
    word_counts = Counter(all_words)
    common_words = word_counts.most_common(10)

    words, counts = zip(*common_words)
    plt.figure(figsize=(8, 6))
    sns.barplot(x=list(words), y=list(counts))
    plt.title('Top 10 Most Common Words in URLs')
    plt.show()

# Main function
def main(file_path):
    # Load data
    df = load_data(file_path)

    # Overview of the dataset
    data_overview(df)

    # Visualizing data
    plot_data_distribution(df)
    plot_feature_distribution(df)
    plot_feature_correlation(df)
    plot_class_balance(df)
    plot_missing_values(df)
    plot_outliers(df)
    plot_feature_distribution_by_class(df)
    plot_pairwise_features(df)
    plot_correlation_with_target(df)
    plot_feature_importance(df)
    plot_url_length_distribution(df)
    plot_common_words_in_url(df)

if __name__ == "__main__":
    # Path to your dataset (CSV)
    file_path = 'datasets/phishing_dataset.csv'
    main(file_path)
