

def build_index(sub: str, file_path: str, api_key: str):
    """
    Build_Index
    
    Intended for use after a metadata tree has been created using route_tree(). Not currently implemented.
    
    :param sub: A string containing the target subdirectory beneath https://api.eia.gov/v2/ (i.e. "petroleum/sum").
    :param file_path: A string with a .rds extension containing the destination path for the completed index, cached locally.
    :param api_key: A string containing your EIA API key.
    
    :return: None
    """
    m_data = eia_meta(sub, api_key)