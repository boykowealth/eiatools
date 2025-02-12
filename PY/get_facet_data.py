import pandas as pd
from eia_meta import eia_meta

def get_facet_data(sub, facet_id, api_key):
    """
    Get facet data

    :param sub: a string containing subdirectory for the EIA API endpoint (string)
    :param facet_id: a string containing the facet ID (string)
    :param api_key: your EIA API key (string)
    :return: A DataFrame containing the facet data
    """
    f_data = eia_meta(sub=f"{sub}/facet/{facet_id}", api_key=api_key)
    # print(f_data['facets'])
    return [facet['id'] for facet in f_data['facets']]