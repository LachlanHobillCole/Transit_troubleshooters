import os
import pandas as pd
import numpy as np

# def read_text_files_to_dataframes(data_path):
#     # Initialise an empty dictionary to store DataFrames
#     dataframes = {}
#     pd.set_option('display.max_columns',None)

#     # Loop through all files in the folder
#     for filename in os.listdir(data_path):
#         if filename.endswith(".txt"):  # reading text files
#             file_path = os.path.join(data_path, filename)
            
#             # Read the text file into a DataFrame
#             df = pd.read_csv(file_path, sep=',')  # Can adjust the separator
            
            
#             # Use the file name (without extension) as the DataFrame name
#             dataframe_name = os.path.splitext(filename)[0]
            
#             # Store the DataFrame in the dictionary with the file name as the key
#             dataframes[dataframe_name] = df

#     return dataframes


# def read_csv_files_to_dataframes(data_path):
#     # Initialise an empty dictionary to store DataFrames
#     csv_dataframes = {}
#     pd.set_option('display.max_columns',None)

#     # Loop through all files in the folder
#     for filename in os.listdir(data_path):
#         if filename.endswith('.csv'):  # reading text files
#             file_path = os.path.join(data_path, filename)
            
#             # Read the text file into a DataFrame
#             df = pd.read_csv(file_path)  # Can adjust the separator
            
            
#             # Use the file name (without extension) as the DataFrame name
#             csv_dataframe_name = os.path.splitext(filename)[0]
            
#             # Store the DataFrame in the dictionary with the file name as the key
#             csv_dataframes[csv_dataframe_name] = df

#     return csv_dataframes


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
