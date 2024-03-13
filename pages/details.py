import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

from scripts.fetch_data import fetch_data
from scripts.process_data import process_data
from components.sidebar import sidebar

# Page Configuration
st.set_page_config(page_title="Statistiques Wevent - Détails des événements", page_icon=":bar_chart:", layout="wide")
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

data: dict = {}

# get the date of the most recent event
last_event_date = raw_data['events'][0]['startDate'].split('T')[0]
if last_event_date > end_date.strftime('%Y-%m-%d'):
    last_event_date = end_date.strftime('%Y-%m-%d')

date = datetime.strptime(start_date.strftime('%Y-%m-%d'), '%Y-%m-%d')
while date <= datetime.strptime(last_event_date, '%Y-%m-%d'):
    data[date.strftime('%Y-%m-%d')] = 0
    date += timedelta(days=1)

for event in raw_data['events']:
    event_date = event['startDate'].split('T')[0]
    if event_date > last_event_date or event_date < start_date.strftime('%Y-%m-%d'):
        continue
    elif event_date in data:
        data[event_date] += 1
    else:
        data[event_date] = 1

df = pd.DataFrame({
    "Jours": list(data.keys()),
    "Evenemements": list(data.values())
})

today = datetime.now().date()
df['Status'] = df['Jours'].apply(lambda x: 'Futur' if datetime.strptime(x, '%Y-%m-%d').date() > today else 'Passé')

# Header
st.title("Statistiques Wevent - Détails des événements")

fig = px.line(df, x="Jours", y="Evenemements", color='Status',
              title="Nombre d'événements par jour",
              color_discrete_map={'Passé': 'blue', 'Futur': 'red'})
st.plotly_chart(fig, use_container_width=True)