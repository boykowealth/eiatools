def map_headers(url, api_key, headers=None):
    """
    Remap Headers

    :param url: A string with the URL endpoint
    :param api_key: A string with your EIA API key
    :param headers: A dictionary with header names and arguments (default is None)
    :return: A string URL with headers mapped
    """
    if headers is None:
        # Adds the API header only!
        return f"{url}?api_key={api_key}"
    else:
        headers['api_key'] = api_key

        # Conversion for known facets and headers:
        conversion_table = {
            'sort': "sort[0][column]",
            'direction': "sort[0][direction]",
            'data': "data[0]",
            'freq': "frequency"
        }

        for key in list(headers.keys()):
            if key in conversion_table:
                headers[conversion_table[key]] = headers.pop(key)

        header_string = "&".join([f"{key}={value}" for key, value in headers.items()])
        return f"{url}?{header_string}"
