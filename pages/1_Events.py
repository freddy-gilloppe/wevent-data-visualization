import streamlit as st
import json
import pandas as pd
from datetime import datetime

def events_demo() -> None:
    events = json.load(open("data/events.json"))

    # Inputs
    st.sidebar.markdown("# Options")
    time_unit = st.sidebar.selectbox("Afficher par", ["Mois", "Semaine", "Jour"])
    start_date = st.sidebar.date_input("Date de début", datetime(2023, 1, 1))
    end_date = st.sidebar.date_input("Date de fin", datetime(2023, 6, 30))  

    filtered_events = [event for event in events if start_date <= datetime.strptime(event["dates"]["start"], "%Y-%m-%d %H:%M:%S").date() <= end_date]

    st.markdown(f"## Events par {time_unit}")
    events_per_unit = {}

    for event in filtered_events:
        start_date = datetime.strptime(event["dates"]["start"], "%Y-%m-%d %H:%M:%S")

        if time_unit == "Jour":
            unit = start_date.strftime("%Y-%m-%d")
        elif time_unit == "Semaine":
            num_week = start_date.strftime("%U")
            unit = f"Semaine {num_week}"
        elif time_unit == "Mois":
            unit = start_date.strftime("%Y-%m")

        if unit in events_per_unit:
            events_per_unit[unit] += 1
        else:
            events_per_unit[unit] = 1
    st.bar_chart(events_per_unit)

    st.markdown(f"## Durée moyenne en heure des Events par {time_unit}")
    durations_per_unit = {}

    for event in filtered_events:
        start_date = datetime.strptime(event["dates"]["start"], "%Y-%m-%d %H:%M:%S")
        end_date = datetime.strptime(event["dates"]["end"], "%Y-%m-%d %H:%M:%S")
        duration = end_date - start_date

        if time_unit == "Jour":
            unit = start_date.strftime("%Y-%m-%d")
        elif time_unit == "Semaine":
            num_week = start_date.strftime("%U")
            unit = f"Semaine {num_week}"
        elif time_unit == "Mois":
            unit = start_date.strftime("%Y-%m")

        # Convertir la durée en heures (timedelta vers float)
        duration_hours = duration.total_seconds() / 3600

        if unit in durations_per_unit:
            durations_per_unit[unit].append(duration_hours)
        else:
            durations_per_unit[unit] = [duration_hours]

    mean_durations_per_unit = {unit: sum(durations_per_unit[unit]) / len(durations_per_unit[unit]) for unit in durations_per_unit}
    st.line_chart(mean_durations_per_unit)

    st.markdown(f"## Répartition des Events sur la carte")
    mapData = []
    for event in filtered_events:
        mapData.append([event["name"], event["location"]["latitude"], event["location"]["longitude"]])
    df = pd.DataFrame(mapData, columns=["name", "latitude", "longitude"])
    st.map(df)

    st.markdown(f"## Seconde carte avec arrondissements")
    st.components.v1.html(open("data/paris_map.html").read(), width=800, height=600)

    events_per_arrondissement = json.load(open("data/events_per_arrondissement.json"))
    st.markdown(f"### Nombre d'Events par arrondissement")
    st.bar_chart(events_per_arrondissement)

    # progress_bar = st.sidebar.progress(0)


st.markdown("# Animation Demo")
with st.expander("Events Json Object", expanded=False):
    st.json({
        "id": "string",
        "name": "string",
        "dates": {
            "start": "date",
            "end": "date"
        },
        "location": {
            "x": "float",
            "y": "float"
        }
    })


events_demo()