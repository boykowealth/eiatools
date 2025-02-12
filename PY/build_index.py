from eia_meta import eia_meta

def build_index(sub: str, api_key: str):
    """
    Build_Index
    
    Intended for use after a metadata tree has been created using route_tree(). Not currently implemented.
    
    :param sub: A string containing the target subdirectory beneath https://api.eia.gov/v2/ (i.e. "petroleum/sum").
    :param api_key: A string containing your EIA API key.
    
    :return: 
    """
    m_data = eia_meta(sub, api_key)
    return m_data