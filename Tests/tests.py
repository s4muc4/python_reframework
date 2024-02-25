import os
import pandas as pd

def read_excel_config(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # Read Excel file
    xls = pd.ExcelFile(file_path)

    # Initialize an empty dictionary to store the configuration
    config = {}

    # Read each tab
    for sheet_name in xls.sheet_names:
        # Read the sheet into a DataFrame
        df = pd.read_excel(xls, sheet_name)

        # Print the DataFrame for debugging
        print(f"Sheet '{sheet_name}' DataFrame:")
        print(df)

        # Convert the DataFrame to a dictionary
        sheet_dict = dict(zip(df['Name'], df['Value']))

        # Add the dictionary to the main config dictionary
        config[sheet_name] = sheet_dict

    return config

# Get the directory where main.py is located
main_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the path to Config.xlsx
config_file_path = os.path.join(main_directory, 'Data', 'Config.xlsx')

# Call the function to read the Excel file and create the config dictionary
config = read_excel_config(config_file_path)

# Print the resulting config dictionary
print("Final Config Dictionary:")
print(config)
