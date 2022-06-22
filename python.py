import csv
import pandas as pd

df=pd.read_csv('merged_data.csv')

del df['Luminosity']
del df['Star_name']
del df['Distance']
del df['Mass']
del df['Radius']
del df['Unnamed: 0']
del df['Unnamed: 6']


df=df.rename({
                'pl_hostname':'solar_system_name',
                'pl_discmethod':'planet_discovery_method',
                'pl_orbincl':'planet_orbital_inclination',
                'pl_dens':'planet_density',
                'ra_str':'right_ascension',
                'dec_str':'declination',
                'st_teff':'host_temperature',
                'st_mass':'host_mass',
                'st_rad':'host_radius'
        },axis='columns')

df.to_csv('main.csv')

