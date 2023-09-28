#%%
import pandas as pd
import numpy as np
from pathlib import Path
import os
from dotenv import load_dotenv
import plotly.express as px

import folium
from folium import PolyLine, Marker


import Data_prep



# %%

load_dotenv(override=True)

# %%
# Example usage
data_path = Path(os.getenv("data_path"))
dataframes = Data_prep.read_files_to_dataframes(data_path)
#csv_dataframes = Data_prep.read_csv_files_to_dataframes(data_path)

# %%
# Can now access each text file as a DataFrame by its file name
for filename, df in dataframes.items():
    print(f"DataFrame Name: {filename}")
    print(df.head())  

# %%
dataframes['routes_1'].head(3)
# %%

# Join the data frames to create a complete data set
merged_data = pd.merge(dataframes['routes'], dataframes['trips'], on='route_id')
merged_data = pd.merge(merged_data, dataframes['stop_times'], on='trip_id')
merged_data = pd.merge(merged_data, dataframes['stops'], on='stop_id')

# %%
shap_trip = pd.merge(dataframes['trips'], dataframes['shapes'], on='shape_id')

# %%


# Create a map centered around a specific location (e.g., Sydney)
m = folium.Map(location=[-33.8688, 151.2093], zoom_start=10)

# Iterate through the data to add route lines
# for route_id, route_data in merged_data.groupby('route_id'):
#     # Extract route coordinates from shape data
#     route_coordinates = route_data[['shape_pt_lat', 'shape_pt_lon']].values.tolist()
#     PolyLine(route_coordinates, color='blue', weight=5).add_to(m)

# Iterate through the data to add bus stops
for stop_data in merged_data[['stop_lat', 'stop_lon', 'stop_name']].drop_duplicates().itertuples():
    Marker([stop_data.stop_lat, stop_data.stop_lon], tooltip=stop_data.stop_name).add_to(m)

# Save the map to an HTML file
m.save('bus_routes_map.html')


# %%
