import time
import requests
import json

def eia_call(endpoint, sleep=5, retries=3):
    """
    Function for handling API requests at an atomic level.
    Also includes URL cleaning components automatically applied by most web browsers.

    :param endpoint: a URL endpoint, with headers attached (string)
    :param sleep: number of seconds to wait before continuing (integer)
    :return: A response in JSON format (dictionary) or an error message.
    """
    for attempt in range(retries):
            response = requests.get(endpoint)
            if response.status_code == 200:
                try:
                    return response.json().get('response', None)
                except json.JSONDecodeError:
                    print("Invalid JSON response")
                    return None
            elif response.status_code == 429:
                print("Rate limited, retrying...")
                time.sleep(2 ** attempt)
            else:
                print(f"Error: {response.status_code}")
                return None
    return None
