import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
import plotly.express as px
import geopandas as gpd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
dtype={'user_id': int}


city_day_data = pd.read_csv("./city_day.csv")
city_hour_data = pd.read_csv("./city_hour.csv")
station_day_data = pd.read_csv("./station_day.csv")
station_hour_data = pd.read_csv("./station_hour.csv")
station_data = pd.read_csv("./stations.csv")


series = ['City' , 'Date' , 'PM2.5' , 'PM10' , 'NO' , 'NO2' , 'CO' , 'SO2' , 'O3' , 'AQI' , 'AQI_Bucket']

city_day_data_req = city_day_data[series].copy()

city_day_data_req.isna().sum().sum()
city_day_newdata_req = city_day_data_req.dropna()

msno.bar(city_day_data)
msno.matrix(city_day_data)
msno.heatmap(city_day_data)

city_hour_new_data = city_hour_data.dropna()
city_day_new_data = city_day_data.dropna()

grouped_df = city_day_data.groupby(['City'])
grouped_df.last()
new_df = grouped_df.last()
new_f_df = grouped_df.first()


# plt.xticks(fontsize=10, rotation=90)
# sns.scatterplot(x = 'City',y = 'PM2.5' ,data = new_df , color = 'red' , marker= 'x')
# pm2_5, ax = plt.subplots(figsize=(10, 6))
# ax.set_xticks(fontsize=10, rotation=90)
# sns.scatterplot(x='City', y='PM2.5', data=new_df, color='red', marker='x', ax=ax)

pm2_5 = plt.figure(figsize=(10, 6))
plt.xticks(fontsize=10, rotation=90)
sns.scatterplot(x='City', y='PM2.5', data=new_df, color='red', marker='x')

pm10 = plt.figure(figsize=(10, 6))
plt.xticks(fontsize=10, rotation=90)
sns.scatterplot(x = 'City',y = 'PM10' ,data = new_df , color = 'purple' , marker= '.')

fp = r'./Maps_with_python-master/india-polygon.shp'
map_df = gpd.read_file(fp) 
map_df_copy = gpd.read_file(fp)
# map_df.head()

merged_city_state = pd.merge(city_day_newdata_req,station_data,on='City',how = 'inner')
grouped_df = merged_city_state.groupby(['City'])
new_df = grouped_df.last()
ser3 = ['PM2.5' , 'State']
req_df = new_df[ser3].copy()
req_df = req_df.sort_values('State')

req_df.reset_index(inplace=True)
All_City = req_df['City']

ans_df = req_df.drop_duplicates(subset = ['State'], keep = 'last')

merged = map_df.set_index('st_nm').join(ans_df.set_index('State'))
merged['PM2.5'] = merged['PM2.5'].replace(np.nan, 0)
merged.head()

india, ax = plt.subplots(1, figsize=(10, 10))
ax.axis('off')
ax.set_title('State-wise Air Quality(PM2.5)', fontdict={'fontsize': '20', 'fontweight' : '10'})
# Plot the figure
merged.plot(column='PM2.5',cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0',legend=True,markersize=[39.739192, -104.990337], legend_kwds={'label': "Number of landslides"})



good = new_f_df[new_f_df['AQI_Bucket'].str.contains("Good")]
gd = good.count()
good.reset_index(inplace=True)
goodcity = good['City']

Satisfactory = new_f_df[new_f_df['AQI_Bucket'].str.contains("Satisfactory")]
Satisfactory.reset_index(inplace=True)
Satisfactorycity = Satisfactory['City']


Moderate = new_f_df[new_f_df['AQI_Bucket'].str.contains("Moderate")]
Moderate.reset_index(inplace=True)
Moderatecity = Moderate['City']

Poor = new_f_df[new_f_df['AQI_Bucket'].str.startswith("Poor")]
Poor.reset_index(inplace=True)
Poorcity = Poor['City']

Very_poor = new_f_df[new_f_df['AQI_Bucket'].str.contains("Very Poor")]
Very_poor.reset_index(inplace=True)
Very_poorcity = Very_poor['City']

Severe = new_f_df[new_f_df['AQI_Bucket'].str.contains("Severe")]
Severe.reset_index(inplace=True)
Severecity = Severe['City']


sd = Satisfactory.count()
md = Moderate.count()
poord = Poor.count()
vpd = Very_poor.count()
sed = Severe.count()
list1 = ["Good" , "Satisfactory" , "Very Poor" , "Severe" , "Poor", "Moderate"]
list2 = [gd.Date , sd.Date , vpd.Date , sed.Date , poord.Date , md.Date]

def detect_aqi(aqi):
      arr = []
      if aqi == 'Good':
            arr = goodcity
      elif aqi == 'Satisfactory':
            arr = Satisfactorycity
      elif aqi == 'Very Poor':
            arr = Very_poorcity
      elif aqi == 'Severe':
            arr = Severecity
      elif aqi == 'Poor':
            arr = Poorcity
      elif aqi == 'Moderate':
            arr = Moderatecity
      return arr

df5 = pd.DataFrame(list(zip(list1,list2)),columns=["AQI_Bucket" , "Number of cities"])

fig = px.pie(df5, values='Number of cities', names='AQI_Bucket', title='Air Quality Condition' , hole=0.7)
fig.add_annotation(dict(x=0.5, y=0.3,  align='center',
                        xref = "paper", yref = "paper",
                        showarrow = False, font_size=22,
                        text="Category"))
fig.add_layout_image(
    dict(
        source="https://png.pngtree.com/element_our/20200702/ourlarge/pngtree-environmental-protection-industry-pollution-building-elements-image_2288148.jpg",
        xref="paper", yref="paper",
        x=0.5, y=0.34,
        sizex=0.4, sizey=0.4,
        xanchor="center", yanchor="bottom", sizing= "contain",
    )
)

airQuality = fig

#Make a graph where user enters the input and then we show the graph related to that input

ser = ["City" , "Date" ,  "PM2.5"  , "PM10"]
city = "Visakhapatnam"
def cityfilter(city):
      city_day_data_PM = city_day_data[ser].copy()
      city_day_data_PM
      city_day_data_PM.dropna(inplace = True)
      city_specific_data = city_day_data_PM[city_day_data_PM['City'] == city]

      fig = px.line(city_specific_data, x="Date", y="PM2.5", title='Air quality vs Time')
      return fig

def cityfilterPM10(city):
      city_day_data_PM = city_day_data[ser].copy()
      city_day_data_PM
      city_day_data_PM.dropna(inplace = True)
      city_specific_data = city_day_data_PM[city_day_data_PM['City'] == city]

      fig = px.line(city_specific_data, x="Date", y="PM10", title='Air quality of city with Time')
      return fig


# para=['StationName', 'StationId']
# station_id_name = station_data[para].copy()

name_id = pd.merge(station_day_data,station_data,on='StationId',how = 'inner')
lst = ['StationName', 'StationId']
station_name_id = pd.DataFrame(name_id[lst])
station_name_id.drop_duplicates(inplace=True)


ser2 = ["StationId" , "Date" ,  "PM2.5"  , "PM10"]

def filterStation(stationid):
      
      station_day_data_PM = station_day_data[ser2].copy()
      station_day_data_PM.dropna(inplace = True)
      station_specific_data = station_day_data_PM[station_day_data_PM['StationId'] == stationid]

      fig = px.line(station_specific_data, x="Date", y="PM10", title='Air quality of stations with Time')
      return fig




# city_day_data_PM = city_day_data[ser].copy()
# city_day_data_PM
# city_day_data_PM.dropna(inplace = True)
# city_specific_data = city_day_data_PM[city_day_data_PM['City'] == city]

# fig = px.line(city_specific_data, x="Date", y="PM2.5", title='Air quality vs Time')
# # fig.show()

# fig = px.line(city_specific_data, x="Date", y="PM10", title='Air quality of city with Time')
# fig.show()

# stationid = "AP001"
# station_day_data_PM = station_day_data[ser2].copy()
# station_day_data_PM.dropna(inplace = True)
# station_specific_data = station_day_data_PM[station_day_data_PM['StationId'] == stationid]

# fig = px.line(station_specific_data, x="Date", y="PM10", title='Air quality of stations with Time')
# fig.show()
