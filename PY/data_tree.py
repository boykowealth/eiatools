import pandas as pd

def data_tree(r_tree: pd.DataFrame, api_key: str) -> pd.DataFrame:
    """
    Processes an EIA metadata tree to fetch and compile data from multiple API endpoints.
    
    :param r_tree: A pandas DataFrame containing API metadata.
    :param api_key: A string containing the EIA API key.
    :return: A pandas DataFrame containing the collected data.
    """
    output = None

    for _, r_row in r_tree.iterrows():
        endpoint = r_row['api_endpoint']
        freq_list = r_row['freq']

        print(endpoint)
        data_out = None

        for f in freq_list:
            print(f"  {f}")

            found_duplicates = False
            d_out = None
            offset = 0

            while not found_duplicates:
                print(f"    {offset}")

                d = eia_data(api_endpoint=endpoint, freq=f, offset=offset, api_key=api_key)

                print("Data fetched")
                print(d.info())

                if not d.empty:
                    if d_out is None:
                        print("Assigned new d_out")
                        d_out = d
                    else:
                        print("Row expanded d_out")
                        d_out = pd.concat([d_out, d], ignore_index=True)

                    r_count = len(d_out)
                    dist_count = len(d_out.drop(columns=['period'], errors='ignore').drop_duplicates())

                    if dist_count < r_count:
                        print("Range narrowed, exiting")
                        found_duplicates = True
                    else:
                        print("Increasing Offset")
                        offset += 5000
                else:
                    print("Exiting due to zero-length list")
                    found_duplicates = True

            if d_out is not None:
                d_out = d_out.drop(columns=['period'], errors='ignore').drop_duplicates()
                d_out['freq'] = f

                if data_out is None:
                    data_out = d_out
                else:
                    data_out = pd.concat([data_out, d_out], ignore_index=True)

        if data_out is not None:
            selected_cols = [
                "api_endpoint", "facets", "data",
                "route_1_id", "route_1_name", "route_1_description",
                "route_2_id", "route_2_name", "route_2_description",
                "route_3_id", "route_3_name", "route_3_description"
            ]
            metadata = r_row[selected_cols].to_frame().T.dropna(axis=1, how='all')
            data_out = pd.concat([data_out.reset_index(drop=True), metadata.reset_index(drop=True)], axis=1)

            if output is None:
                output = data_out
            else:
                output = pd.concat([output, data_out], ignore_index=True)

    return output.assign(nickname=None).reset_index(drop=True)
