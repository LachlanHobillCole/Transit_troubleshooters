# %%
import pandas as pd
import numpy as np
from pathlib import Path
import os
from dotenv import load_dotenv
import plotly.express as px

import folium
from folium import PolyLine, Marker
import requests
import zipfile
import Data_prep
import Calculations
import Data


#%%
import requests

from google.transit import gtfs_realtime_pb2
from google.protobuf.json_format import MessageToDict
from google.protobuf.json_format import MessageToJson

from protobuf_to_dict import protobuf_to_dict

load_dotenv()

FILENAME_SCHEDULE = 'gtfs.zip'
app_name = os.getenv("APP_NAME")
api_key = os.getenv("API_KEY")
BASE_URL = "https://api.transport.nsw.gov.au"
BUS_POSITION_URI = f"{BASE_URL}/v1/gtfs/vehiclepos/buses"
BUS_SCHEDULE_URI = f"{BASE_URL}/v1/gtfs/schedule/buses"
FERRY_POSITION = f"{BASE_URL}/v1/gtfs/historical"
headers = {
    "Authorization": f"apikey {api_key}"
}
request_details = dict(
    headers=headers,
    stream=True
)

cert = os.getenv("CERT", True)
request_details['verify'] = cert

response = requests.get(BUS_SCHEDULE_URI, **request_details)
response



# %%

load_dotenv(override=True)
cert_path = os.getenv("CERT_PATH", True) # True forces full verificationmy_request['verify'] = cert_path

# %%
# Example usage
data_path = Path(os.getenv("data_path"))
dataframes = Data_prep.read_files_to_dataframes(data_path)
# csv_dataframes = Data_prep.read_csv_files_to_dataframes(data_path)

# %%
# Can now access each text file as a DataFrame by its file name
for filename, df in dataframes.items():
    print(f"DataFrame Name: {filename}")
    print(df.head())

# %%
dataframes["trips"].head(10)
# dataframes['trips'].query("route_id == '2503_7001'")

# %%
# dataframes['agency'].to_csv('agency.csv', index=False)


# %%

# # Join the data frames to create a complete data set
merged_data = pd.merge(dataframes["stop_times"], dataframes["trips"], on="trip_id")
merged_data = pd.merge(merged_data, dataframes["stops"], on="stop_id")
merged_data = pd.merge(merged_data, dataframes["routes"], on="route_id")
merged_data = pd.merge(merged_data, dataframes["agency"], on="agency_id")


# List of agency codes
agency_codes = [
    701,
    2433,
    2434,
    2436,
    2437,
    69,
    2435,
    2445,
    2446,
    2447,
    2448,
    2449,
    2450,
    "B011",
    "B047",
    "B012",
    "B062",
    "B052",
    "B055",
    "B082",
    "B041",
    "B010",
    "B066",
    "B061",
    "B040",
    "B053",
    "B073",
    "B065",
    "B067",
    "B054",
    "B058",
    "B057",
    "B013",
    "B086",
    "WHC",
    "B048",
    "B004",
    "B060",
    "B050",
    "B005",
    "B056",
    "B001",
    "B084",
    "B072",
    "B069",
    "B059",
    "BVC",
    2452,
    2453,
    2457,
    "f",
    2458,
    75,
    710,
    "B044",
    "B014",
    "B021",
    "B007",
    "B045",
    "B034",
    121,
    89,
    88,
    122,
    72,
    79,
    123,
    82,
    "B015",
    "B032",
    "B009",
    "B037",
    "B024",
    "B075",
    "B018",
    "B020",
    "B038",
    "B033",
    "B036",
    "B079",
    74,
    "B003",
]

# Create a mapping dictionary with "bus" as the value for all agency codes
agency_mapping = {code: "bus" for code in agency_codes}

merged_data["Bus_flag"] = merged_data["agency_id"].map(agency_mapping)
Combined_bus_data = merged_data.query("Bus_flag == 'bus'")


# %%


# Combined_bus_data = pd.merge(Combined_bus_data,dataframes['shapes'], on='shape_id')
Combined_bus_data = pd.merge(Combined_bus_data, dataframes["calendar"], on="service_id")
Combined_bus_data = pd.merge(Combined_bus_data, dataframes["agency"], on="agency_id")

# %%
# shap_trip = pd.merge(dataframes['trips'], dataframes['shapes'], on='shape_id')

# %%
# Create a map centered around a specific location (e.g., Sydney)
m = folium.Map(location=[-33.8688, 151.2093], zoom_start=10)

# Iterate through the data to add route lines
for route_id, route_data in Combined_bus_data.groupby("route_id"):
    # Extract route coordinates from shape data
    route_coordinates = route_data[["stop_lat", "stop_lon"]].values.tolist()
    PolyLine(route_coordinates, color="blue", weight=5).add_to(m)

# Iterate through the data to add bus stops
for stop_data in (
    Combined_bus_data[["stop_lat", "stop_lon", "stop_name"]]
    .drop_duplicates()
    .itertuples()
):
    Marker(
        [stop_data.stop_lat, stop_data.stop_lon], tooltip=stop_data.stop_name
    ).add_to(m)

# Save the map to an HTML file
m.save("bus_routes_map.html")


# %%
emission_factors = Calculations.Emission_Factor()

fuel_type = "Diesel"
CO2_emissions = emission_factors.get_emission_factor(fuel_type)
if CO2_emissions is not None:
    print(f"Emission factor for {fuel_type}:{CO2_emissions}")
# %%
