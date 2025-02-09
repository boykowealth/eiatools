import pandas as pd
from map_headers import map_headers
from eia_call import eia_call

default_headers = {
    'sort': 'period',
    'direction': 'desc',
    'data': 'value',
    'length': '5000'
}

def eia_map(sub, offset, freq, api_key):
    """
    EIA Mapping Request

    :param sub: String containing subdirectory for EIA endpoint
    :param offset: Used to offset pagination in sets of 5000 (integer)
    :param api_key: String with your EIA API key (string)
    :param freq: String with an EIA frequency code (string)
    :return: A DataFrame containing the unique identifiers for updated/recent data for products
    """
    root = "https://api.eia.gov/"
    path = f"{root}{sub}"
    headers = default_headers.copy()
    headers.update({'offset': offset, 'freq': freq})

    request = map_headers(url=path, api_key=api_key, headers=headers)
    response = eia_call(request)
    data = response['data']

    deselect_list = ["period", "value"]
    data = pd.DataFrame(data)

    for des in deselect_list:
        if des in data.columns:
            data = data.drop(columns=[des])

    data = data.drop_duplicates()

    return data