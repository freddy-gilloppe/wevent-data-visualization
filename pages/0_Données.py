from datetime import datetime, timedelta
import streamlit as st
import json
import random
import geopandas as gpd
import folium

from shapely.geometry import Point

def regenerate() -> None:
    st.markdown("# Regénérer les données")
    st.markdown(
        """
        ## Paramètres
        Vous pouvez modifier les paramètres pour générer des données différentes.  
        Les données seront générées dans le fichier `data/events.json`.
    """
    )
    col1, col2, col3 = st.columns(3)
    with col1:
        number_of_events = st.number_input("**Nombre d'événements**", min_value=1, max_value=10000, value=100)
    with col2:
        start_date = st.date_input("Date de début", datetime(2023, 1, 1))
    with col3:
        end_date = st.date_input("Date de fin", datetime(2023, 6, 30))
    col1, col2= st.columns(2)
    with col1:
        latitude_range = st.slider("Latitude", -0.1, 0.1, (-0.06, 0.06), 0.001)
    with col2:
        longitude_range = st.slider("Longitude", -0.1, 0.1, (-0.08, 0.08), 0.001)
    
    if st.button("Générer les nouvelles données"):
        # Fichier Json
        generate_events(start_date, end_date, number_of_events, latitude_range, longitude_range)
        
        # Carte Folium
        paris_arrondissements = gpd.read_file("data/paris_arrondissements.geojson")
        m = folium.Map(location=[48.8566, 2.3522], zoom_start=12)
        folium.GeoJson(paris_arrondissements).add_to(m)
        
        events = json.load(open("data/events.json"))

        for event in events:
            lat = event["location"]["latitude"]
            lon = event["location"]["longitude"]
            name = event["name"]
            folium.Marker([lat, lon], popup=name).add_to(m)

        # create an array with for each arrondissement the number of events
        events_per_arrondissement = {}
        for event in events:
            lat = event["location"]["latitude"]
            lon = event["location"]["longitude"]
            point = Point(lon, lat)
            for i, arrondissement in paris_arrondissements.iterrows():
                num_arrondissement = arrondissement["nom"].split(" ")[1]
                num_arrondissement = "".join([c for c in num_arrondissement if c.isdigit()])
                if len(num_arrondissement) == 1:
                    num_arrondissement = "0" + num_arrondissement
                if point.within(arrondissement.geometry):
                    try:
                        events_per_arrondissement[num_arrondissement+"e"] += 1
                    except KeyError:
                        events_per_arrondissement[num_arrondissement+"e"] = 1
                    break

        json.dump(events_per_arrondissement, open("data/events_per_arrondissement.json", "w"), indent=4)

        m.save("data/paris_map.html")

        # End
        st.success("Données générées avec succès !")
        with st.expander("Afficher les 5 premières lignes"):
            events = json.load(open("data/events.json"))
            st.write(events[:5])
        st.balloons()
    
def generate_events(start_date: datetime, end_date: datetime, number_of_events: int, latitude_range: list, longitude_range: list) -> None:
    names = [f"{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}" for i in range(26) for j in range(26) for k in range(26)]

    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 6, 30)

    json_objects = []
    for i in range(1, number_of_events+1):
        name = names[i - 1]
        random_start = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        random_end = random_start + timedelta(hours=random.randint(1, 24))
        latitude = 48.864716 + random.uniform(latitude_range[0], latitude_range[1])
        longitude = 2.349014 + random.uniform(longitude_range[0], longitude_range[1])

        json_obj = {
            "id": str(i),
            "name": name,
            "dates": {
                "start": random_start.strftime("%Y-%m-%d %H:%M:%S"),
                "end": random_end.strftime("%Y-%m-%d %H:%M:%S")
            },
            "location": {
                "latitude": round(latitude, 6),
                "longitude": round(longitude, 6)
            }
        }
        json_objects.append(json_obj)

    with open("data/events.json", "w") as f:
        json.dump(json_objects, f, indent=4)
    return json_objects

regenerate()