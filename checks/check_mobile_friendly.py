import requests
import json
from requests.exceptions import RequestException, HTTPError

def check_mobile_friendly(website: str, api_key: str) -> str:
    """
    Check if the given website is mobile-friendly using the Google Mobile-Friendly Test API.

    Args:
        website (str): The URL of the website to be checked.
        api_key (str): The API key for accessing the Google Mobile-Friendly Test API.

    Returns:
        str: 
            - "🟢" if the website is mobile-friendly.
            - "🔴" if the website is not mobile-friendly.
            - "⚪" for any errors.
    """
    api_url = f"https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run?key={api_key}"
    payload = {"url": f"https://{website}"}
    headers = {'Content-Type': 'application/json'}

    try:
        # Make a POST request to the Google API
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()

        # Parse the response JSON
        result = response.json()

        # Check if the site is mobile-friendly
        if result.get('mobileFriendliness') == 'MOBILE_FRIENDLY':
            print(f"Website {website} is mobile-friendly.")
            return "🟢"
        else:
            print(f"Website {website} is not mobile-friendly.")
            return "🔴"

    except (requests.HTTPError, requests.RequestException) as e:
        print(f"Error occurred while checking mobile-friendliness for {website}: {e}")
        return "⚪"
    except KeyError:
        print(f"Unexpected response format from the API for {website}.")
        return "⚪"
    except Exception as e:
        print(f"An unexpected error occurred while checking mobile-friendliness for {website}: {e}")
        return "⚪"
