import pandas as pd
import numpy as np

def route_tree(sub="", api_key=None, iter=1, iter_offset=1):
    """
    EIA Meta Data Tree

    :param sub: A subdirectory on EIA's API URL, for example, "petroleum" (string)
    :param api_key: Your EIA API key (string)
    :param iter: A counter used in recursion, internal to the function (integer)
    :param iter_offset: A reindexing value used in recursion, internal to the function (integer)
    :return: A metadata DataFrame
    """
    print(sub)
    output = pd.DataFrame()
    m_data = eia_meta(sub=sub, api_key=api_key)

    if iter == 1 and (sub == "" or sub is None):
        iter_offset = 0

    if detect_routes(m_data=m_data):
        routes = get_routes(m_data)

        for i, row in routes.iterrows():
            next_path = f"{sub}/{row['id']}"
            layer_out = route_tree(sub=next_path, api_key=api_key, iter=iter + 1, iter_offset=iter_offset)
            layer_out[f"route_{iter + iter_offset}_id"] = row['id']

            if "name" in routes.columns:
                layer_out[f"route_{iter + iter_offset}_name"] = row['name']
            if "description" in routes.columns:
                layer_out[f"route_{iter + iter_offset}_description"] = row['description']

            output = pd.concat([output, layer_out], ignore_index=True)
    else:
        api_endpoint = sub
        freqs = get_all_freq(m_data=m_data)
        facet_types = get_facet_types(m_data=m_data)
        data_types = get_data_types(m_data=m_data)

        if isinstance(data_types, list) and len(data_types) == 0:
            data_types = np.nan

        if m_data.get('startPeriod') is None:
            m_data['startPeriod'] = np.nan
        if m_data.get('endPeriod') is None:
            m_data['endPeriod'] = np.nan

        layer_out = pd.DataFrame({
            "api_endpoint": [api_endpoint],
            "freq": [freqs],
            "facets": [facet_types],
            "data": [data_types],
            "start_period": [m_data['startPeriod']],
            "end_period": [m_data['endPeriod']]
        })

        for f in facet_types:
            facet_data = get_facet_data(sub=sub, facet_id=f, api_key=api_key)

            if not (isinstance(facet_data, list) and len(facet_data) == 0):
                layer_out[f] = [facet_data]

        output = layer_out

    if iter == 1 and not (sub == "" or sub is None):
        if "name" in m_data:
            output["route_1_name"] = m_data["name"]
        if "id" in m_data:
            output["route_1_id"] = m_data["id"]
        if "description" in m_data:
            output["route_1_description"] = m_data["description"]

    return output