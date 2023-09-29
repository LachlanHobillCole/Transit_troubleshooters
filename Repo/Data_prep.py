import os
import pandas as pd
import numpy as np


def read_files_to_dataframes(data_path):
    # Initialize an empty dictionary to store DataFrames
    dataframes = {}
    pd.set_option('display.max_columns', None)

    # Loop through all files in the folder
    for filename in os.listdir(data_path):
        if filename.endswith((".txt", ".csv")):  # Check for both .txt and .csv files
            file_path = os.path.join(data_path, filename)
            
            # Read the file into a DataFrame
            if filename.endswith(".txt"):
                df = pd.read_csv(file_path, sep=',')  # Adjust the separator for text files
            elif filename.endswith(".csv"):
                df = pd.read_csv(file_path)  # Read CSV files without specifying separator
            
            # Use the file name (without extension) as the DataFrame name
            dataframe_name = os.path.splitext(filename)[0]
            
            # Store the DataFrame in the dictionary with the file name as the key
            dataframes[dataframe_name] = df

    return dataframes

# Define the BusFleetData class
class BusFleetData:
    def __init__(self):
        self.bus_data = []

    def get_bus_info(self, bus_id):
        # Retrieve information about a specific bus
        for bus in self.bus_data:
            if bus['bus_id'] == bus_id:
                return bus
            


