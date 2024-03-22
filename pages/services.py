import streamlit as st

from components.sidebar import sidebar

# Configuration de la page
st.set_page_config(page_title="Statistiques Wevent - Services", page_icon=":bar_chart:", layout="wide")
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

# Titre de la section
st.header("Statistiques Wevent - État des services")

services_etats = {
    "Statistiques Wevent": "running",
    "Serveur API": "running",
    "Base de donnée Mongo": "running",
    "Azure DevOps": "running"
}

# Mapping des états aux emojis
etat_emoji = {
    "running": "🟢", # :green_circle:
    "down": "🔴", # :red_circle:
    "maintenance": "🟡" # :yellow_circle:
}

# Affichage des états des services avec emojis
for service, etat in services_etats.items():
    emoji = etat_emoji.get(etat, "❓")
    st.markdown(f"{emoji} **{service}**: {etat}", unsafe_allow_html=True)
