import requests
import pandas as pd

def eia_version(api_key):
    url = f"https://api.eia.gov/v2?api_key={api_key}"
    response = requests.get(url).json()
    
    # Ensure 'apiVersion' is at the correct level
    api_version = response.get('apiVersion', 'Unknown version')
    excel_version = response.get('ExcelAddInVersion', 'Unknown version')

    versions = [['EIA API Version', api_version], ['Excel AddIn Version', excel_version]]
    
    print(pd.DataFrame(versions))
    return api_version, excel_version

