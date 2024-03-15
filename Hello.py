import streamlit as st
from components.sidebar import sidebar

def run():
    st.set_page_config(page_title="Statistiques Wevent", page_icon=":bar_chart:", layout="wide")

    sidebar(st)

    st.write("# Statistiques Wevent")

    st.markdown("""### Accédez aux données en cliquant sur le bouton "Données".""")
    st.markdown("---")
    st.markdown("*La documentation générale de Wevent est disponible [ici](https://dev.azure.com/hadjiai/Wevent).*")
    st.markdown("*Pour plus de détails sur les statistiques ou l'interface, consultez la documentation spécialisée [ici](https://dev.azure.com/hadjiai/Wevent/_git/Wevent-dataViz).*")


if __name__ == "__main__":
    run()
