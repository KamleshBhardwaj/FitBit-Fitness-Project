# -*- coding: utf-8 -*-
"""Minutes activity merged.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xPJg8ZYveeISXps-IwQPSvceFkqRgWJV
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

minute_Calories_Narrow_merged = pd.read_csv('/content/drive/MyDrive/minuteCaloriesNarrow_merged.csv')
minute_Intensities_Narrow_merged = pd.read_csv('/content/drive/MyDrive/minuteIntensitiesNarrow_merged.csv')
minuteMET_sNarrow_merged = pd.read_csv('/content/drive/MyDrive/minuteMETsNarrow_merged.csv')
minuteSteps_Narrow_merged = pd.read_csv('/content/drive/MyDrive/minuteStepsNarrow_merged.csv')

minute_Calories_Narrow_merged.head()

minute_Intensities_Narrow_merged.head()

minuteSteps_Narrow_merged.head()

minuteMET_sNarrow_merged.head()

#Merge Dataset
merged_df = pd.merge(minute_Calories_Narrow_merged, minute_Intensities_Narrow_merged, on=['Id', 'ActivityMinute'])
merged_df = pd.merge(merged_df, minuteMET_sNarrow_merged, on=['Id', 'ActivityMinute'] , how = 'outer')
Minute_Activity_df = pd.merge(merged_df, minuteSteps_Narrow_merged, on=['Id', 'ActivityMinute'] , how = 'outer')

#Display Dataset
Minute_Activity_df.head()

Minute_Activity_df.info()

#Check Duplicate Values
Minute_Activity_df.duplicated().sum()

# Convert ActivityMinute and format
Minute_Activity_df['ActivityMinute'] = pd.to_datetime(Minute_Activity_df['ActivityMinute'])
Minute_Activity_df['ActivityMinute'] = pd.to_datetime(Minute_Activity_df['ActivityMinute']).dt.strftime('%m/%d/%Y')
Minute_Activity_df['ActivityMinute'] = Minute_Activity_df['ActivityMinute'].str.replace('/', '-')

Minute_Activity_df.head()

Minute_Activity_df.describe()

"""# Install Pandas Profiling"""

pip install pandas-profiling

import pandas as pd
from ydata_profiling import ProfileReport

# Now create the profile report
Profile = ProfileReport(Minute_Activity_df, title="Minutes Activity Reports", html={'style':{'full_width':True}})

Profile

#Save the merged dataset to a new CSV file
Minute_Activity_df.to_csv('Minute_Activity_merged.csv', index=False)

