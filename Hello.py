import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="Wevent Data Visualization",
        page_icon="utils/icon.png",
    )

    st.markdown("![Logo Wevent](https://dev.azure.com/hadjiai/ca64f8a4-cacc-4800-bfd7-4c00931de1ac/_apis/git/repositories/909a176e-8254-435a-8bb6-05467816beea/Items?path=/.attachments/Asset%204%403x%201-64911039-948b-4bf3-bfc2-e4601933b855.png&download=false&resolveLfs=true&%24format=octetStream&api-version=5.0-preview.1&sanitize=true)")
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
