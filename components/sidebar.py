

def sidebar(st: object) -> None:
    st.sidebar.page_link("Accueil.py", label="Accueil")
    st.sidebar.markdown("---")
    st.sidebar.page_link("pages/general.py", label=":chart_with_upwards_trend: Données Générales")
    st.sidebar.page_link("pages/details.py", label=":bar_chart: Détails des événements")
    st.sidebar.page_link("pages/maps.py", label=":world_map: Données géographiques")
    st.sidebar.markdown("---")
    st.sidebar.page_link("pages/services.py", label=":zap: État des services")