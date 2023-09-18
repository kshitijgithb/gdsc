import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

global_data = pd.read_csv("./global air pollution dataset.csv")

global_data.sort_values(['Country'] , inplace=True)
global_high_aqi = global_data.drop_duplicates(subset = ['Country'], keep = 'first')
series = ['Country' , 'AQI Value']
global_high_aqi_country_AQI = global_high_aqi[series].copy()
global_high_aqi_country_AQI.dropna(inplace=True)


fig = px.scatter_geo(global_high_aqi_country_AQI,locations='Country',locationmode='country names',
                     size="AQI Value",color='Country',title="AQI value Countries"
                     )
fig.update_geos(projection_type="orthographic")

aqi_country = fig


grouped_df = global_data.groupby(['Country'])
new_f_df = grouped_df.last()
new_f_df.reset_index(inplace = True)


good = new_f_df[new_f_df['AQI Category'].str.contains("Good")]
gd = good.count()
Moderate = new_f_df[new_f_df['AQI Category'].str.contains("Moderate")]
Poor = new_f_df[new_f_df['AQI Category'].str.startswith("Unhealthy for")]
unhealth = new_f_df[new_f_df['AQI Category'].str.endswith("Unhealthy")]
Hazardous = new_f_df[new_f_df['AQI Category'].str.contains("Hazardous")]
Very_unhealthy = new_f_df[new_f_df['AQI Category'].str.contains("Very Unhealthy")]
hd = Hazardous.count()
md = Moderate.count()
poord = Poor.count()
vhd = Very_unhealthy.count()
ud = unhealth.count()
# sed = Severe.count()
list1 = ["Good" , "Moderate" , "Unhealthy for sensitive groups" , "Very Unhealthy" , "Hazardous" , "Unhealthy"]
list2 = [gd['AQI Value'] , md['AQI Value'] ,poord['AQI Value'], hd['AQI Value'] ,vhd['AQI Value'] , ud["AQI Value"]]

def detect_aqi(aqi):
      arr = []
      if aqi == 'Good':
            arr = good['Country']
      elif aqi == 'Moderate':
            arr = Moderate['Country']
      elif aqi == 'Unhealthy for sensitive groups':
            arr = Poor['Country']
      elif aqi == 'Very Unhealthy':
            arr = Very_unhealthy['Country']
      elif aqi == 'Hazardous':
            arr = Hazardous['Country']
      elif aqi == 'Unhealthy':
            arr = unhealth['Country']
      return arr



df5 = pd.DataFrame(list(zip(list1,list2)),columns=["AQI Category" , "Number of countries"])


fig = px.pie(df5, values='Number of countries', names='AQI Category', title='Countries vs AQI Categories')
country_aqi_pie = fig
# fig.show()

fig = px.scatter_geo(new_f_df,locations='Country',locationmode='country names'
                     ,color='AQI Category',title="AQI value Countries"
                     )

fig.update_geos(projection_type="natural earth")
aqi_catergory_grp = fig
# fig.show()


#Cities with respective AQI Category
good = new_f_df[new_f_df['AQI Category'].str.contains("Good")].sort_values(['Country'])
Moderate = new_f_df[new_f_df['AQI Category'].str.contains("Moderate")].sort_values(['Country'])
Poor = new_f_df[new_f_df['AQI Category'].str.startswith("Unhealthy for")].sort_values(['Country'])
unhealth = new_f_df[new_f_df['AQI Category'].str.endswith("Unhealthy")].sort_values(['Country'])
Hazardous = new_f_df[new_f_df['AQI Category'].str.contains("Hazardous")].sort_values(['Country'])
Very_unhealthy = new_f_df[new_f_df['AQI Category'].str.contains("Very Unhealthy")].sort_values(['Country'])
choose_category = good

def detect_city_aqi(aqi):
      choose_category = []

      if aqi == 'Good':
            choose_category = good
      
      elif aqi == 'Moderate':
            choose_category = Moderate
            
      elif aqi == 'Unhealthy for sensitive groups':
            choose_category = Poor
            
      elif aqi == 'Very Unhealthy':
            choose_category = Very_unhealthy
            
      elif aqi == 'Hazardous':
            choose_category = Hazardous
            
      elif aqi == 'Unhealthy':
            choose_category = unhealth

      para = ['City', 'Country']
      arr = pd.DataFrame(choose_category[para])
      return arr


# print(choose_category['City'] + "  " + choose_category['Country'])