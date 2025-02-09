import time
import requests
import json

def eia_call(endpoint, sleep=5):
    """
    Function for handling API requests at an atomic level.
    Also includes URL cleaning components automatically applied by most web browsers.

    :param endpoint: a URL endpoint, with headers attached (string)
    :param sleep: number of seconds to wait before continuing (integer)
    :return: A response in JSON format (dictionary)
    """
    endpoint = endpoint.replace(" ", "%20")

    print(endpoint)
    response = requests.get(endpoint)
    response_content = response.content.decode('utf-8')
    response_json = json.loads(response_content)

    time.sleep(sleep)

    return response_json['response']
