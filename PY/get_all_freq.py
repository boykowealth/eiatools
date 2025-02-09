def get_all_freq(m_data):
    """
    Get all frequency codes

    :param m_data: A dictionary with EIA metadata
    :return: A list of frequency codes applicable to the EIA API
    """
    # print(m_data['frequency']['id'])
    return m_data['frequency']['id']
