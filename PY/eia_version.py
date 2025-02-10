from map_headers import map_headers
from eia_call import eia_call

def eia_version(api_key):
    import requests
    
    url = f"https://api.eia.gov/v2?api_key={api_key}"
    response = requests.get(url).json()
    
    # Ensure 'apiVersion' is at the correct level
    api_version = response.get('apiVersion', 'Unknown version')
    excel_version = response.get('ExcelAddInVersion', 'Unknown version')

    versions = [['EIA API Version', api_version], ['Excel AddIn Version', excel_version]]
    
    print(versions)
    return api_version, excel_version