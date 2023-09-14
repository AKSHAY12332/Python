import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px

file_path='WHO-COVID-19.csv'
df = pd.read_csv(file_path)
#print(df)

country=df['Country/Region']
cases = df['Confirmed']

data = df.groupby("Country/Region")['Confirmed'].sum().reset_index()



fig=plt.figure(figsize=(10,15))

# Creating the bar plot

plt.bar(country, cases, color ='maroon', width=1.0)
plt.xlabel("Country/Region")
plt.ylabel("Confirmed Cases")
plt.title("Covid-19 Report Respective to the Country")
plt.show()

china_data= df[df['Country/Region'] == 'China'].drop(['Country/Region'],axis=1)
china_data = china_data[china_data.sum(axis=1)>0]

china_data = china_data.groupby(['Province/State'])['Confirmed'].sum().reset_index()
state_fig = px.bar(china_data, x='Province/State', y='Confirmed', title='State wise confirmed cases in China')
state_fig.show()