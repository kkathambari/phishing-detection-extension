import sys
import os

# Add the src directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from feature_extraction import extract_features




def test_extract_features():
    """
    Test the feature extraction process for various URLs.
    """
    test_urls = [
        "https://example.com",  # Legitimate URL
        "http://malicious-site.com/path?query=value",  # Malicious-looking URL
        "https://short.url",  # Potentially shortened URL
        "http://www.phishing-test-site.org/login",  # Phishing-looking URL
        "https://secure-login-page.com",  # Legitimate-looking secure URL
    ]

    for url in test_urls:
        features = extract_features(url)
        print(f"URL: {url}")
        print("Extracted Features:\n", features)

if __name__ == "__main__":
    test_extract_features()
