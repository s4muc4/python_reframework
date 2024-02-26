from Components.logs import *
from datetime import datetime
import shutil
import os
import pandas as pd

def buildReport():
    logMessage("[buildReport] - Started", "INFO")

    hash, time = retrieveHashCodeProject()

    reportPathTemplate = "./Data/Report_Template.xlsx"
    reportPath = "./Reports/"
    reportFileName = f"Report_{time}_{hash}.xlsx"
    reportFullPath = reportPath + reportFileName

    shutil.copy(reportPathTemplate, reportPath)

    destination_path = os.path.join(reportPath, os.path.basename(reportPathTemplate))

    os.rename(destination_path, os.path.join(reportPath, reportFileName))

    logMessage("[buildReport] - Ended", "INFO")
    return reportFullPath

def updateReport(filePath, reference, startTime, endTime, status, details):
    logMessage("[updateReport] - Started", "INFO")
    sheetName = "Report"
    newData = {'Reference': reference, 'Start': startTime, 'End': endTime, 'Status': status, 'Details': details}
    
    

    df = pd.read_excel(filePath, sheet_name=sheetName)
    
    if reference in df['Reference'].values:
        df.loc[df['Reference'] == reference] = [newData['Reference'], newData['Start'], newData['End'], newData['Status'], newData['Details']]
    else:
        df = df._append(newData, ignore_index=True)

    df.to_excel(filePath, sheet_name=sheetName, index=False)

    logMessage("[updateReport] - Ended", "INFO")