import panadas as pd
def get_routes(m_data):
    """
    Get routes dataframe from EIA metadata

    :param m_data: A dictionary with EIA metadata
    :return: A DataFrame containing the routes data
    """
    return pd.DataFrame(m_data['routes'])
