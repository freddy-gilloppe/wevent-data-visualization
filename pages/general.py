import streamlit as st
import pandas as pd
import plotly.express as px
from scripts.fetch_data import fetch_data
from scripts.process_data import process_data
from components.sidebar import sidebar

# Fetch and process data
raw_data = fetch_data()
processed_data = process_data(raw_data)

# Page Configuration
st.set_page_config(page_title="Statistiques Wevent - Données générales", page_icon=":bar_chart:", layout="wide")
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

# Header
st.title("Statistiques Wevent - Données générales")

st.markdown(
    f"""
    <div style="background-color:#f0f2f6; border-radius:10px; padding: 10px; margin-bottom: 20px;">
        <h3 style="text-align:center; color:#333;">👤 Utilisateurs en ligne: {processed_data['onlineUsers']}</h3>
    </div>
    """, unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("<p class='big-font'>Nombre d'événements</p>", unsafe_allow_html=True)
    st.subheader(format(processed_data['number_of_events'], ".0f"))

with col2:
    st.markdown("<p class='big-font'>Nombre moyen de participants par événement</p>", unsafe_allow_html=True)
    st.subheader(format(processed_data['mean_number_of_participants'], ".2f"), help=str(processed_data['mean_number_of_participants']))

col1, col2 = st.columns(2)

with col1:
    st.markdown("<p class='big-font'>Nombre d'événements gratuits</p>", unsafe_allow_html=True)
    st.subheader(format(processed_data['number_of_free_events'], ".0f"))

with col2:
    st.markdown("<p class='big-font'>Prix moyen des événements payants</p>", unsafe_allow_html=True)
    # st.subheader(processed_data['mean_price_without_free'])
    st.subheader(format(processed_data['mean_price_without_free'], ".2f") + " €", help=str(processed_data['mean_price_without_free']))

# Plotting with Plotly
top_categories_df = pd.DataFrame(list(processed_data['top_categories'].items()), columns=['Categories', 'Count'])
fig = px.bar(top_categories_df, x='Categories', y='Count')
st.plotly_chart(fig, use_container_width=True)