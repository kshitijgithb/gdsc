import numpy as np
import pandas as pd
import streamlit as st
import global_support as gsup
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)



st.set_page_config(page_title="Global Air Pollution Analysis", page_icon='https://cdn3d.iconscout.com/3d/premium/thumb/green-earth-6855145-5625018.png?f=webp')

st.sidebar.title("Global Air Pollution Analysis")

st.sidebar.markdown('''
<style>
    .sidebar {
  margin: 0;
  padding: 0;
  width: 18rem;
  position: fixed;
  height: 100%;
  overflow: auto;
  
  margin-top: 2rem;
  border-radius: 0;
}

.sidebar a {
  display: block;
  color: black;
  padding: 12px;
  text-decoration: none;
  background-color: #f5f6f5;
  border-radius: 0;
  border-bottom: 4px solid rgb(0 67 30);
}

.sidebar a.active {
  background-color: #04AA6D;
  color: white;
}

.sidebar a:hover:not(.active) {
  background-color: #555;
  color: white;
}

div.content {
  margin-left: 200px;
  padding: 1px 16px;
  height: 1000px;
}

@media screen and (max-width: 700px) {
  .sidebar {
    width: 100%;
    height: auto;
    position: relative;
  }
  .sidebar a {float: left;}
  div.content {margin-left: 0;}
}

@media screen and (max-width: 400px) {
  .sidebar a {
    text-align: center;
    float: none;
  }
}
.iconss{
    height: 20px;
    width: 20px;
}
</style>
<div class="sidebar">
  <a class="" href="#home">
    <img class="iconss" src="https://i.pinimg.com/originals/d7/34/6c/d7346c03444c44944cf2f5b5674ccf27.png">
    Home
  </a>
  <a href="https://waterpotabilitytest.divyarani13.repl.co/">
    <img class="iconss" src="https://www.freeiconspng.com/uploads/water-services-icon-11.png">
    Water Prediction
  </a>
  <a href="https://wasteclassification-1--divyarani13.repl.co/">
    <img class="iconss" src="https://seeklogo.com/images/R/recycle-symbol-label-logo-1B79A2B5B8-seeklogo.com.png">
    Garbage Classification
  </a>
  
</div>
''', unsafe_allow_html=True)



page_bg_img = '''
<style>
body {
background-image: url("https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/abstract-waves-cool-sabarton.jpg");
background-size: cover;
}
</style>
'''

set_bg_image = """
      <style>
        *{
            border-radius: 10px;
        }
        [data-testid="stAppViewContainer"] {
            background-image: url('https://media.istockphoto.com/id/1289562025/vector/dark-green-background-with-small-touches-christmas-texture-with-vignette-on-the-sides-and.jpg?s=612x612&w=0&k=20&c=AyUlGOhur7Su8xWtu-3eTx3Nup4YEj-sRT6Wj-e-4nw=');
            background-image: url('https://images.unsplash.com/photo-1571389246213-f7e66cb3d6b3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Z3JlZW4lMjBmbG93ZXJ8ZW58MHx8MHx8fDA%3D&w=1000&q=80');
            background-image: url('https://img3.wallspic.com/crops/6/5/7/7/2/127756/127756-tulip-wildflower-flower-yellow-natural_landscape-4928x3280.jpg');
            background-image: url('https://cdn.wallpapersafari.com/46/7/fYyxuW.jpg');
            background-image: url('https://files.123freevectors.com/wp-content/original/148190-dark-green-wave-background-image.jpg');
            background-size: cover;
        }
        [data-testid="block-container"]{
            /*background-color: white;
            padding: 3rem 1rem 5rem;*/
        }
        [data-testid="stMarkdownContainer"]{
            /*background-color: whitesmoke;
            padding: 0.2rem 0.5rem 0rem;
            margin-bottom: 0.1rem*/
        }
        .header-img{
            height: 4rem;
            width: 100%;
        }
        .stSelectbox > [data-baseweb="select"] div{
            background-color: white;
            color: black;
        }
        [data-baseweb="popover"] div{
            background-color: white;
            color: black;
        }
        
        [data-baseweb="icon"]
        {
            color: black;
        }
        [data-testid="stHeader"]{
            background-color: #062e06;
        }
        .stPlotlyChart .js-plotly-plot
        {
            background-color: white;
        }
        [data-testid="block-container"]{
            padding: 2rem 1rem 3rem;
        }
        footer
        {
            visibility: hidden;
        }
      </style>
      """
st.markdown(set_bg_image,unsafe_allow_html=True)


st.markdown("""
<style>
[data-testid="stSidebar"]{
    background-image: url('https://media.istockphoto.com/id/1289562025/vector/dark-green-background-with-small-touches-christmas-texture-with-vignette-on-the-sides-and.jpg?s=612x612&w=0&k=20&c=AyUlGOhur7Su8xWtu-3eTx3Nup4YEj-sRT6Wj-e-4nw=');
}
</style>
    """, unsafe_allow_html=True)

st.title('Global Air Pollution Analysis')

st.write('Understanding global air pollution analysis is crucial as air pollution transcends borders and affects the health and environment of people worldwide. It provides valuable insights into the collective impact of pollution on a planetary scale, driving international cooperation to combat its adverse effects. Additionally, global analysis empowers individuals and policymakers with data-driven knowledge, fostering responsible actions to mitigate pollution and safeguard the well-being of future generations.')

st.image('https://ral.ucar.edu/sites/default/files/public/images/features/cities.png')

st.subheader('AQI Value Across the World')
st.write("AQI values across the world often reveal alarming levels of pollution, with countries like China, Bangladesh, and Pakistan frequently experiencing hazardous air quality conditions. These regions grapple with severe pollution challenges, emphasizing the need for comprehensive air quality management strategies. Despite these challenges, many countries are actively implementing measures to improve air quality and protect their citizens' health.")

st.subheader('International Air Quality Range')
st.image('https://oizom.com/wp-content/uploads/2019/08/4-2.png')
aqi_country = gsup.aqi_country
st.plotly_chart(aqi_country)

bucket =  gsup.list1
aqi = st.selectbox('Select a AQI Bucket', bucket)

arr = gsup.detect_aqi(aqi)
st.dataframe(arr)

st.plotly_chart(gsup.country_aqi_pie)
st.plotly_chart(gsup.aqi_catergory_grp)

bucket2 = gsup.list1
aqicc = st.selectbox('Select a AQI county Bucket', bucket2)
city = gsup.detect_city_aqi(aqicc)
st.dataframe(city)


st.markdown(
      '''

    <div style="width: 100%; border-radius: 0; background-image: url('https://files.123freevectors.com/wp-content/original/161337-lime-green-texture-background.jpg'); background-size: cover; display: flex;flex-direction: column; justify-content: center; align-items: center; flex-wrap: wrap; padding: 2rem;">
            <img style="width: 400px; margin-bottom: 1rem; border-radius: 0;" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmjF9Z-Ylbz8DdpjAe2oI3R3sONeUcrfOSBQ&usqp=CAU" alt="">
            <div class="text-center p-3" style="display: flex;border-radius: 0; align-items: center; font-family: 'Rubik', sans-serif;
            justify-content: center; padding: 1rem;   color: white; background-color: rgba(0, 0, 0, 0.2);"> © 2023 Copyright:
                  <a style="text-decoration: none; color: white;" href="https://github.com/abhik813/Ecothon-EcoTech">Team Spam Bytes</a>
            </div>
      </div>

''', unsafe_allow_html=True
)
