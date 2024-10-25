import pandas as pd
import streamlit as st
import plotly.express as px
from termcolor import colored
from streamlit_js_eval import bootstrapButton, get_geolocation


DATASET_URL = "https://dagshub.com/Omdena/VITBhopalUniversity_ChatbotforBRTSNavigation/raw/99c2e8d2883dd9faaa68ed60d5405dd40e77c456/src/tasks/task-2/Routes/all_routes_combined.csv"

df = pd.read_csv(DATASET_URL)
df['Size'] = 5
df['Color'] = '#800080'


st.set_page_config(page_title="Bhopal University Chatbot for BRTS Navigation", page_icon="📚", layout="wide")

st.write("""
<style>
    .mapboxgl-ctrl-bottom-right, .mapboxgl-ctrl-bottom-left {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

check_location = st.checkbox("Check my location")

if check_location:
    loc = get_geolocation()
    if loc is not None:
        user_lat, user_long = loc['coords']['latitude'], loc['coords']['longitude']
    
        additional_point = pd.DataFrame({
            'Latitude': user_lat,
            'Longitude': user_long,
            'Color': ['#ff0000'],
            'Size': [10]
        })

        df = pd.concat([df, additional_point])

st.map(
    data=df,
    color='Color',
    size='Size',
    height=500,
    latitude='Latitude',
    longitude='Longitude',
    zoom=4 if check_location else 10,
)