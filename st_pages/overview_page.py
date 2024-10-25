import humanize
import warnings
import pandas as pd
import streamlit as st
import plotly.express as px
warnings.filterwarnings('ignore')

from constants import LANDMARK_COLORS

overview = None

def main(overview):
    overview.write("<h3>📊 Overview Of BRTS Dataset</h3>", unsafe_allow_html=True)
    a1, a2, a3, a4, input_area, dl_csv = overview.columns([0.65,0.65,0.65,1,1.5,0.6])

    try:
        og_df = pd.read_csv("assets/data/all_routes_combined.csv")
        df = og_df.copy()
        
        df['Size'] = 5
        df['Color'] = df['Route'].map(lambda x: LANDMARK_COLORS[x]['hex'])

        selected_route = input_area.selectbox("Select a Route", ['All', *LANDMARK_COLORS])

        a1.metric("Total Stations", df.shape[0])
        a2.metric(":red[SR Routes]", 8)
        a3.metric(":blue[TR Routes]", 4)
        a4.metric(":green[Selected Route Stations]", df.shape[0] if selected_route == 'All' else df[df['Route'] == selected_route].shape[0])

        csv = df.to_csv(index=False).encode('utf-8')
        dl_csv.write("<br>"*1, unsafe_allow_html=True)
        dl_csv.download_button("Download Data", data=csv, file_name="all_routes_combined.csv", mime="text/csv", use_container_width=True)
        
        cols = overview.columns([1,0.7])

        with cols[0]:
            st.dataframe(og_df, height=420, use_container_width=True)
        with cols[1]:
            st.map(df, latitude="Latitude", longitude="Longitude", color="Color", height=420, size='Size')
            
    except IndexError:
        overview.dataframe(df, height=200)

if __name__ == '__main__':
    main()