import streamlit as st
import pandas as pd
import streamlit as st
import os as os

#Obligatoire 1ere ligne de la page
st.set_page_config(page_title="Mon Projet Streamlit", layout="wide")

# Charger le CSS personnalisé
def load_css(file_path):
    abs_path = os.path.join(os.getcwd(), file_path)  # Chemin absolu
    with open(abs_path, "r") as f:
        css = f"<style>{f.read()}</style>"
        st.markdown(css, unsafe_allow_html=True)

# Appliquer le CSS
load_css("assets/style.css")

# ###################### Configuration de la page

# Titre
st.write("je suis la page reco.")

# Récupérer la valeur sélectionnée dans la page principale
if "selected_option" in st.session_state:
    selected_option = st.session_state["selected_option"]
    st.write(f"Vous avez sélectionné : **{selected_option}**")
else:
    st.warning("Aucune option n'a été sélectionnée.")