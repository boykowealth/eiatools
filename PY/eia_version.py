from map_headers import map_headers
from eia_call import eia_call

def eia_version(api_key):
    """
    EIA Version Request

    :param api_key: A string containing your EIA API Key (string)
    :return: A dictionary containing API and Excel Versions for EIA's web service (dictionary)
    """
    root = "https://api.eia.gov/"
    url = map_headers(api_key=api_key)
    response = eia_call(url)

    return {
        'api': response['apiVersion'],
        'excel': response['ExcelAddInVersion']
    }