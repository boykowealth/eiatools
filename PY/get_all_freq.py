def get_all_freq(m_data):
    """
    Get all frequency codes

    :param m_data: A dictionary with EIA metadata
    :return: A list of frequency codes applicable to the EIA API
    """
    # print(m_data['frequency']['id'])
    # print(type(m_data['frequency']))
    # print(m_data['frequency'])
    return [freq['id'] for freq in m_data['frequency']]
