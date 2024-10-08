# -*- coding: utf-8 -*-
"""Weight_Heart.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/164F1V4ISnUESRCVADOteciJXHU6qttMm

# Weight_Log
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Weight_LogInfo_merged = pd.read_csv('/content/drive/MyDrive/weightLogInfo_merged.csv')

Weight_LogInfo_merged.head()

#Check null valuea
#Weight_LogInfo_merged.isnull().sum()

Weight_LogInfo_merged.info()

Weight_LogInfo_merged.describe()

Weight_LogInfo_merged.duplicated().sum()

Weight_LogInfo_merged['Date'] = pd.to_datetime(Weight_LogInfo_merged['Date'])
Weight_LogInfo_merged.info()

#Code Extract Time
Weight_LogInfo_merged["Date"].dt.time

Weight_LogInfo_merged['Hour'] = Weight_LogInfo_merged['Date'].dt.time
Weight_LogInfo_merged.head()

# Convert Date and format
Weight_LogInfo_merged['Dates'] = pd.to_datetime(Weight_LogInfo_merged['Date'])
Weight_LogInfo_merged['Dates'] = pd.to_datetime(Weight_LogInfo_merged['Date']).dt.strftime('%m/%d/%Y')

Weight_LogInfo_merged.head()

del Weight_LogInfo_merged['Dates']

Weight_LogInfo_merged.head()

"""Heart Rate"""

Heart_Rate_second = pd.read_csv('/content/drive/MyDrive/heartrate_seconds_merged.csv')

Heart_Rate_second.head()

Heart_Rate_second.info()

Heart_Rate_second["Time"] = pd.to_datetime(Heart_Rate_second["Time"])
Heart_Rate_second.info()

#Code Extract  Time
Heart_Rate_second["Time"].dt.time

Heart_Rate_second["Hours"] = Heart_Rate_second["Time"].dt.time
Heart_Rate_second.head()

# Convert ActivityMinute and format
Heart_Rate_second['Date'] = pd.to_datetime(Heart_Rate_second['Time'])
Heart_Rate_second['Date'] = pd.to_datetime(Heart_Rate_second['Time']).dt.strftime('%m/%d/%Y')

Heart_Rate_second.head()

del Heart_Rate_second['Time']

Heart_Rate_second.head()

#Check null valuea
Heart_Rate_second.isnull().sum()

#Save the merged dataset to a new CSV file
Weight_LogInfo_merged.to_csv('Weights_LogInfo_merged.csv', index=False)
Heart_Rate_second.to_csv('Heart_Rates_second.csv', index=False)

