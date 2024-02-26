from Components.logs import logMessage
import pandas as pd
import os
from Components.finalReport import buildReport


def initAllSettings(file_path):

    logMessage("[initAllSettings] - Started", "INFO")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    xls = pd.ExcelFile(file_path)
    config = {}

    for sheet_name in xls.sheet_names:
        # Read the sheet into a DataFrame
        df = pd.read_excel(xls, sheet_name)

        # Convert each row of the DataFrame to a dictionary
        sheet_dict = df.set_index('Name')['Value'].to_dict()

        # Update the main config dictionary with the sheet dictionary
        config.update(sheet_dict)

    config = {key: value for key, value in config.items() if pd.notna(key)}

    config['reportPath']=buildReport()


    logMessage(F"{len(config)} items in config", "TRACE")
    logMessage("[initAllSettings] - Ended", "INFO")

    return config
