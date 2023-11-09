import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Wevent Data Visualization"
    )

    st.markdown("![Logo Wevent](https://drive.google.com/file/d/1-heyeYfvCrpxiusfUDk3cITvjrFeEUG8/view?usp=sharing)")
    st.write("# Data Visualization")

    st.markdown(
        """
        - Commencez par générer des données en cliquant sur le bouton "Données".
        - Accédez aux graphiques en cliquant sur le bouton "Events".   
        ---
        [Page de Wevent](https://dev.azure.com/hadjiai/Wevent)
    """
    )


if __name__ == "__main__":
    run()
