import requests

def test_phishing_detection(url):
    """
    Sends a GET request to the Flask server for URL classification.
    """
    # Flask API endpoint URL
    api_url = f'http://localhost:5000/classify?url={url}'

    try:
        # Send the GET request
        response = requests.get(api_url)

        # Check the response status
        if response.status_code == 200:
            result = response.json()
            print(f"URL: {result['url']}")
            print(f"Prediction: {result['result']}")
        else:
            print(f"Error: {response.json()['error']}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    test_urls = [
        # Phishing websites
        "http://www.paypal.com.secure-login-update.com",  # phishing
        "https://www.bankofamerica.account-security.com",  # phishing
        "http://www.amazon.com.update-security.verify.com",  # phishing
        "https://www.google.com.account-suspension-notice.com",  # phishing
        "http://www.microsft.com.security-upgrade.com",  # phishing
        "https://www.facebook.com.login-verify-check.com",  # phishing
        "http://www.apple.com.account-verify-update.com",  # phishing
        "https://www.paypal.com.security-update-account.com",  # phishing
        "http://www.netflix.com.secure-login-update.com",  # phishing
        "https://www.twitter.com.security-warning.com",  # phishing

        # Legitimate websites
        "https://www.linkedin.com",  # legitimate
        "https://www.paypal.com",  # legitimate
        "https://www.amazon.com",  # legitimate
        "https://www.google.com",  # legitimate
        "https://www.microsoft.com",  # legitimate
        "https://www.facebook.com",  # legitimate
        "https://www.apple.com",  # legitimate
        "https://www.netflix.com",  # legitimate
        "https://www.twitter.com",  # legitimate
        "https://www.github.com",  # legitimate

    ]
    
    for url in test_urls:
        test_phishing_detection(url)