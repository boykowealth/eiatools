def get_facet_types(m_data):
    """
    Get facet codes

    :param m_data: A dictionary with EIA metadata
    :return: A list of facet codes applicable to the EIA API
    """
    return m_data['facets']['id']
