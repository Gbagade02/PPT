import requests
import pandas as pd

def download_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to download data. Status code: {response.status_code}")

def convert_to_csv(data, output_file):
    df = pd.DataFrame(data)
    
    # Rename the columns
    column_mapping = {
        'name': 'Name of Earth Meteorite',
        'id': 'id',
        'meteorite': 'Meteorite',
        'nametype': 'nametype',
        'recclass': 'recclass',
        'mass (g)': 'mass',
        'year': 'year',
        'reclat': 'reclat',
        'reclong': 'reclong'
    }
    df = df.rename(columns=column_mapping)
    
    
    # Save dataframe to CSV
    df.to_csv(output_file, index=False)

# Main program
url = 'https://data.nasa.gov/resource/y77d-th95.json'
output_file = 'meteorites.csv'

try:
    data = download_data(url)
    convert_to_csv(data, output_file)
    print(f"Data has been downloaded and saved as {output_file}")
except Exception as e:
    print(f"An error occurred: {str(e)}")