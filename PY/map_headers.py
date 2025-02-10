def map_headers(url, api_key, headers=None):
    """
    Remap Headers to URL Parameters

    :param url: A string with the URL endpoint
    :param api_key: A string with your EIA API key
    :param headers: A dictionary with parameter names and arguments (default is None)
    :return: A formatted URL with query parameters
    """
    if headers is None:
        headers = {}

    # Ensure API key is included
    headers["api_key"] = api_key

    # Conversion table for known parameters
    conversion_table = {
        "sort": "sort[0][column]",
        "direction": "sort[0][direction]",
        "data": "data[0]",
        "freq": "frequency"
    }

    # Convert headers based on the mapping
    updated_headers = {
        conversion_table.get(key, key): value for key, value in headers.items()
    }

    # Construct the query string
    query_string = "&".join(f"{key}={value}" for key, value in updated_headers.items())
    
    return f"{url}?{query_string}"
