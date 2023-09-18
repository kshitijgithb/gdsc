import numpy as np
import pandas as pd
import streamlit as st
import support
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

st.set_page_config(page_title="Air Pollution Analysis", page_icon='https://cdn3d.iconscout.com/3d/premium/thumb/green-earth-6855145-5625018.png?f=webp')

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
        [data-testid="stDataFrameResizable"]
      </style>
      """
st.markdown(set_bg_image,unsafe_allow_html=True)

st.markdown("""
<style>
[data-testid="stSidebar"]{
    background-image: url('https://images.unsplash.com/photo-1571389246213-f7e66cb3d6b3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Z3JlZW4lMjBmbG93ZXJ8ZW58MHx8MHx8fDA%3D&w=1000&q=80');
    background-image: url('https://media.istockphoto.com/id/1289562025/vector/dark-green-background-with-small-touches-christmas-texture-with-vignette-on-the-sides-and.jpg?s=612x612&w=0&k=20&c=AyUlGOhur7Su8xWtu-3eTx3Nup4YEj-sRT6Wj-e-4nw=');
}
footer
{
    visibility: hidden;
}
[data-testid="block-container"]{
            padding: 2rem 1rem 3rem;
}
</style>
    """, unsafe_allow_html=True)


st.title('Air Pollution Analysis')
st.write("Understanding the significance of air pollution analysis is paramount in today's world. Air pollution is a global concern that affects the health and well-being of individuals and the environment alike. By delving into air pollution analysis using Python, we gain valuable insights into the quality of the air we breathe. This knowledge empowers us to make informed decisions, advocate for cleaner air, and take steps towards mitigating the adverse effects of pollution on our health and the planet. In essence, air pollution analysis is not merely a scientific endeavor; it is a call to action for a healthier and more sustainable future for all.")

st.video('https://www.youtube.com/watch?v=n-f8a3ihmSE')

st.subheader('PM2.5')
st.write('PM2.5, or Particulate Matter 2.5, is a critical air quality parameter that refers to tiny airborne particles with a diameter of 2.5 micrometers or less. These particles are so small that they can easily penetrate deep into the lungs and even enter the bloodstream when inhaled. PM2.5 is a significant concern in air pollution analysis as it includes various harmful substances like dust, smoke, and pollutants.')

pm2_5fig = support.pm2_5
st.pyplot(pm2_5fig)
st.markdown("<i><h6 style='text-align: center; color: white; margin-top: -2rem;'>City v/s PM2.5 plot</h6></i>", unsafe_allow_html=True)

st.image(
      "https://cdn-cenii.nitrocdn.com/dxZQGVjeOyXblsYkcsxiHEoJOLKUvtcl/assets/images/optimized/rev-a677aee/www.pranaair.com/wp-content/uploads/2021/08/health-imapcts-of-pm2.5-pollution.png",
)

st.subheader('PM10')
st.write('PM10, or Particulate Matter 10, represents another crucial parameter in air quality analysis. These microscopic particles, with a diameter of 10 micrometers or less, are found in the air we breathe and can have a significant impact on our health. PM10 includes a range of materials, from dust and pollen to soot and allergens.')

pm10fig = support.pm10
st.pyplot(pm10fig)
st.markdown("<i><h6 style='text-align: center; color: white; margin-top: -2rem; background: white'>City v/s PM10 plot</h6></i>", unsafe_allow_html=True)
st.image(
      "https://cdn.shortpixel.ai/client/to_webp,q_glossy,ret_img,w_1280,h_720/https://smartairfilters.com/wordpress/wp-content/uploads/2019/04/Particle-Sizes-Virus-Labelled.jpg",
)
st.markdown("<h6 style='text-align: center; color: grey; margin-top: -2rem; background: white'>PM2.5 vs. PM10: The Difference in Particle Air Pollution</h6>", unsafe_allow_html=True)

st.write('''

''')


india = support.india
st.pyplot(india)
st.markdown("<div style='text-align: center; color: grey; background: white'>Air quality in India exhibits substantial variation across states. For instance, states like Himachal Pradesh and Kerala typically enjoy better air quality owing to their cleaner environments and lower industrialization. In contrast, states such as Delhi and Uttar Pradesh often grapple with severe pollution issues due to urbanization and industrial emissions. Each state adopts specific measures to address its unique air quality challenges, reflecting the diverse efforts made to safeguard public health.</div>", unsafe_allow_html=True)


st.subheader('AQI Bucket')
st.write('AQI (Air Quality Index) buckets categorize air quality into different ranges, such as "Good," "Moderate," "Unhealthy," and "Hazardous," to help people understand the level of pollution in their area easily.')
st.image('https://www.indiatogether.org/uploads/picture/image/2590/IT_airquality.png')


bucket =  support.list1
aqi = st.selectbox('Select a Bucket', bucket)

arr = support.detect_aqi(aqi)
st.dataframe(arr)

st.plotly_chart(support.airQuality)


st.subheader("Discover Your City's Air Wellness")

st.sidebar.title("India Air Quality Analysis")

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


original_list = support.All_City
result = st.selectbox('Choose Your city', original_list)
fig = support.cityfilter(result)
fig2 = support.cityfilterPM10(result)
st.plotly_chart(fig)
st.plotly_chart(fig2)


station_list = support.station_name_id
station_name_only = station_list['StationId']
selected_station = st.selectbox('Choose your Station', station_name_only)
st.write(f'Selected station is {selected_station}')
# stationid = station_list[station_list['StationName'] == selected_station]

# selected_station = str(selected_station)
aqStation = support.filterStation(selected_station)
st.plotly_chart(aqStation)

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
