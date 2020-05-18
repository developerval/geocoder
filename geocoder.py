from geopy.geocoders import ArcGIS
from geopy.exc import GeocoderTimedOut
import pandas

"""
Create a function that will create a pandas dataframe out of the file given, and then add the long and lat columns
to the dataframe. This will need to return the html from the dataframe as it will be passed to the success function
to render on the page once a valid CSV file has been uploaded
"""


def output_gen(input_file):
    nom = ArcGIS(scheme='http')
    df = pandas.read_csv(input_file)
    if 'Address' in df.columns or 'address' in df:
        coords = df['Address' or 'address'].apply(nom.geocode)
        df['Longitutde'] = coords.apply(lambda x: x.longitude)
        df['Latitude'] = coords.apply(lambda x: x.latitude)
        html = df.to_html()
        output = df.to_csv('output.csv')
        return html, output
    else:
        return False
