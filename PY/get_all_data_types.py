def get_data_types(m_data):
    """
    Get data codes

    :param m_data: A dictionary with EIA metadata
    :return: A list of data codes applicable to the EIA API
    """
    return list(m_data['data'].keys())
