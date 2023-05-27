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
    return df

# Main program
url = 'https://data.nasa.gov/resource/y77d-th95.json'
output_file = 'meteorites.csv'

try:
    data = download_data(url)
    df = convert_to_csv(data, output_file)
    print(f"Data has been downloaded and saved as {output_file}")
except Exception as e:
    print(f"An error occurred: {str(e)}")


#Q1. Get all the Earth meteorites that fell before the year 2000
meteorites_that_fell_before_the_year_2000= df[df['year'] < '2000']

#Q2.Get all the earth meteorites co-ordinates who fell before the year 1970
before_the_year_1970 = df[df['year'] < '1970']

#Q3.Assuming that the mass of the earth meteorites was in kg, get all those whose mass was more than 10000kg
df['mass'] = pd.to_numeric(df['mass'])
mass_was_more_than_10000kg = df[df['mass'] > 10000]