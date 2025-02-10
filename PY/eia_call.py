import time
import requests
import json

def eia_call(endpoint, sleep=5):
    """
    Function for handling API requests at an atomic level.
    Also includes URL cleaning components automatically applied by most web browsers.

    :param endpoint: a URL endpoint, with headers attached (string)
    :param sleep: number of seconds to wait before continuing (integer)
    :return: A response in JSON format (dictionary) or an error message.
    """
    endpoint = endpoint.replace(" ", "%20")

    print(f"Requesting: {endpoint}")
    response = requests.get(endpoint)

    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return None  # Handle non-200 responses

    try:
        response_json = response.json()
    except json.JSONDecodeError:
        print("Error: API response is not valid JSON.")
        return None

    # Check if 'response' key exists before returning
    if 'response' not in response_json:
        print("Unexpected API response format:", response_json)
        return None

    time.sleep(sleep)
    return response_json['response']
