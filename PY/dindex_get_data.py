import pandas as pd

from eia_data import eia_data

def dindex_get_data(dindex_table, api_key, start=None, end=None):
    """
    A function accepting rows from the data_index object and then fetches data from EIA

    :param dindex_table: a subset of the data_index table (Pandas DataFrame)
    :param api_key: your EIA API key (string)
    :param start: start date "YYYY-MM-DD" (string)
    :param end: end date "YYYY-MM-DD" (string)
    :return: A DataFrame containing the fetched data
    """
    data_out = pd.DataFrame()

    for i, d_row in dindex_table.iterrows():
        loop = True
        dat_out = pd.DataFrame()
        offset = 0

        while loop:
            f_list = d_row['facets']
            facet_df = pd.DataFrame()

            for f in f_list:
                f_id = d_row[f]
                facet_row = {'facet_name': f, 'facet_id': f_id}
                facet_df = pd.concat([facet_df, pd.DataFrame([facet_row])], ignore_index=True)

            facet_df = facet_df[facet_df['facet_id'] != '#N/A']
            facet_df = facet_df[facet_df['facet_id'] != '(NA)']

            d_out = eia_data(
                api_endpoint=d_row['api_endpoint'],
                freq=d_row['freq'],
                facets=facet_df,
                start=start,
                end=end,
                sort_df=pd.DataFrame({'sortby': ['period'], 'direction': ['desc']}),
                data_types=d_row['data'],
                offset=offset,
                api_key=api_key
            )

            d_out['nickname'] = d_row['nickname']

            if not len(d_out) == 5000:
                loop = False
            else:
                offset += 5000

            dat_out = pd.concat([dat_out, d_out], ignore_index=True)

        dat_out = pd.concat([dat_out, d_out], ignore_index=True)

    return data_out
