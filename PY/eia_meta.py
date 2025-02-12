from eia_call import eia_call

def eia_meta(sub, api_key):
    """
    EIA Metadata Request

    :param sub: A string containing subdirectory, or tree of subdir filepaths for the EIA API endpoint (string)
    :param api_key: String with your EIA API key (string)
    :return: A list containing the JSON data (dictionary)
    """
    root = "https://api.eia.gov/v2/"
    url = f"{root}{sub}?api_key={api_key}"
    response = eia_call(url)
    return response
