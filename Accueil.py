import streamlit as st

def run():
    st.set_page_config(
        page_title="Wevent Statistics"
    )

    st.write("# Wevent Statistics")

    st.markdown("""### Accédez aux données en cliquant sur le bouton "Données".""")
    st.markdown("---")
    st.markdown("*La documentation générale de Wevent est disponible [ici](https://dev.azure.com/hadjiai/Wevent).*")
    st.markdown("*Pour plus de détails sur les statistiques ou l'interface, consultez la documentation spécialisée [ici](https://dev.azure.com/hadjiai/Wevent/_git/Wevent-dataViz).*")


if __name__ == "__main__":
    run()