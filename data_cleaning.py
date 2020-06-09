# The dataset is taken from John Hopkins University's Github Repository

import pandas as pd
print("Startig Data Preprocessing...........")
df = pd.read_csv("COVID-19\\csse_covid_19_data\\csse_covid_19_time_series\\time_series_covid19_confirmed_global.csv")
df = df.drop(["Province/State", "Lat", "Long"], axis = 1) # drop Unnecessory columns
df= df.T                                                   # Transpose the dataset so that the date becomes a column and ever country becomes a column
df.reset_index(level=0, inplace=True)                     # The Row that contains columns became index so this line is converting it to column by reseting index
df = df.rename(columns=df.iloc[0]).drop(df.index[0])      # Making first row column names
df = df.rename(columns={'Country/Region': 'Date'})      # Changing the name of Column "Country/Region" to Date because it contains Dates
df["Date"] = pd.to_datetime(df['Date'])                 # Converting the Date Column's data type to Pandas datetime
df["Week"] = df["Date"].dt.week                         # Extracting the week number from Date Column
df["Week"] = [week -3 for week in df["Week"]]           # The Dataset is starting from 4th week of january so this line is converting the 4th week into first week and so on
df = df.groupby(df.columns, axis=1).sum()               # There were multiple columns of same countries became the orignal dataset had province or state wise Dataset so summing them up to a single column
df = df.infer_objects()                                 # converting the datatype of all the columns with object datatype to int
df_by_weeks = df.groupby(['Week'],as_index=False).last() # Only taking the value of the value of last day of every week now the dataset have weekly data
df_by_weeks.to_csv("covid19_confirmed_cases.csv")


df = pd.read_csv("COVID-19\\csse_covid_19_data\\csse_covid_19_time_series\\time_series_covid19_deaths_global.csv")
df = df.drop(["Province/State", "Lat", "Long"], axis = 1)
df= df.T
df.reset_index(level=0, inplace=True)
df = df.rename(columns=df.iloc[0]).drop(df.index[0])
df = df.rename(columns={'Country/Region': 'Date'})
df["Date"] = pd.to_datetime(df['Date'])
df["Week"] = df["Date"].dt.week
df["Week"] = [week -3 for week in df["Week"]]
df = df.groupby(df.columns, axis=1).sum()
df = df.infer_objects()
df_by_weeks = df.groupby(['Week'],as_index=False).last()
df_by_weeks.to_csv("covid19_deaths.csv")


df = pd.read_csv("COVID-19\\csse_covid_19_data\\csse_covid_19_time_series\\time_series_covid19_recovered_global.csv")
df = df.drop(["Province/State", "Lat", "Long"], axis = 1)
df= df.T
df.reset_index(level=0, inplace=True)
df = df.rename(columns=df.iloc[0]).drop(df.index[0])
df = df.rename(columns={'Country/Region': 'Date'})
df["Date"] = pd.to_datetime(df['Date'])
df["Week"] = df["Date"].dt.week
df["Week"] = [week -3 for week in df["Week"]]
df = df.groupby(df.columns, axis=1).sum()
df = df.infer_objects()
df_by_weeks = df.groupby(['Week'],as_index=False).last()
df_by_weeks.to_csv("covid19_recovered.csv")

print("Data Cleaning Done")
