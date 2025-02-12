import pandas as pd
from eia_call import eia_call

def eia_data(api_endpoint, freq, facets=None, start=None, end=None, sort_df=None, data_types=None, offset=None, api_key=None):
    """
    Fetch data from the EIA API

    :param api_endpoint: an EIA API endpoint subdirectory (string)
    :param freq: a valid EIA frequency for the endpoint (string)
    :param facets: a DataFrame with cols facet_name, facet_id (Pandas DataFrame)
    :param start: a string in "YYYY-MM-DD" format (string)
    :param end: a string in "YYYY-MM-DD" format (string)
    :param sort_df: a DataFrame with sortby=column_name and direction=c(asc,desc) columns (Pandas DataFrame)
    :param data_types: a list of valid datatypes to pull (list)
    :param offset: a numeric for pagination of results (integer)
    :param api_key: your EIA API key (string)
    :return: A DataFrame containing the fetched data
    """
    root = "https://api.eia.gov/v2/"
    api_req = f"{root}{api_endpoint}/data?api_key={api_key}&length=5000"
    
    # Adding start header
    if start:
        api_req += f"&start={start}"
    
    # Adding end header
    if end:
        api_req += f"&end={end}"
    
    # Adding offset
    if isinstance(offset, int) and offset > 0:
        api_req += f"&offset={offset}"
    
    # Adding data column names
    if data_types:
        for i, data_type in enumerate(data_types):
            api_req += f"&data[{i}]={data_type}"
    
    # Adding facets from facet df
    if facets is not None:
        for i, row in facets.iterrows():
            api_req += f"&facets[{row['facet_name']}][]={row['facet_id']}"
    
    # Adding sort params
    if sort_df is not None:
        for i, row in sort_df.iterrows():
            api_req += f"&sort[{i}][column]={row['sortby']}&sort[{i}][direction]={row['direction']}"
    
    output = eia_call(api_req)
    return pd.DataFrame(output.get('data', []))
