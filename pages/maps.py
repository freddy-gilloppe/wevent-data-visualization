import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

from scripts.fetch_data import fetch_data
from scripts.process_data import process_data
from scripts.geo import listCountries
from components.sidebar import sidebar

# Page Configuration
st.set_page_config(page_title="Statistiques Wevent - Données géographiques", page_icon=":bar_chart:", layout="wide")
st.markdown(
    """
    <style>
    .big-font {
        font-size:20px !important;
    }
    </style>
    """, unsafe_allow_html=True
)

sidebar(st)

# Inputs
st.sidebar.markdown("# Options")
start_date = st.sidebar.date_input("Date de début", datetime(2023, 1, 1))
end_date = st.sidebar.date_input("Date de fin", datetime(2024, 12, 31))

# Fetch and process data
raw_data = fetch_data(start_date, end_date)
processed_data = process_data(raw_data)

# Header
st.title("Statistiques Wevent - Données géographiques")

df_coordinates = pd.DataFrame(processed_data['coordinates'], columns=['lat', 'lon'])

# Display the map
st.map(df_coordinates)

# Plotting countries with Plotly
st.markdown("<p class='big-font'>Pays</p>", unsafe_allow_html=True)
countries = pd.DataFrame(listCountries(raw_data['events']).items(), columns=['Countries', 'Count'])
fig = px.bar(countries, x='Countries', y='Count')
st.plotly_chart(fig, use_container_width=True)
