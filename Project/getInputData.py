from Components.logs import logMessage
import pandas as pd


def getInputData(path,sheet):
    logMessage("[getInputData] - Started", "INFO")

    df = pd.read_excel(path, sheet_name=sheet)
    print(df)

    logMessage("[getInputData] - Ended", "INFO")
    return df




