import os
import pandas as pd
import numpy as np

def read_text_files_to_dataframes(data_path):
    # Initialise an empty dictionary to store DataFrames
    dataframes = {}
    pd.set_option('display.max_columns',None)

    # Loop through all files in the folder
    for filename in os.listdir(data_path):
        if filename.endswith(".txt"):  # reading text files
            file_path = os.path.join(data_path, filename)
            
            # Read the text file into a DataFrame
            df = pd.read_csv(file_path, sep=',')  # Can adjust the separator
            
            
            # Use the file name (without extension) as the DataFrame name
            dataframe_name = os.path.splitext(filename)[0]
            
            # Store the DataFrame in the dictionary with the file name as the key
            dataframes[dataframe_name] = df

    return dataframes


