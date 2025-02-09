def detect_routes(m_data):
    """
    Detect routes

    Determine if the routes key is present in the metadata
    :param m_data: A dictionary containing metadata
    :return: Boolean
    """
    return "routes" in m_data.keys()
