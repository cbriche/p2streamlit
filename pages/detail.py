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
st.write("je suis la page détail.")

# Récupérer les paramètres de l'URL
image_name = st.query_params.get("image_name", "Aucune image sélectionnée")

# Titre
st.title("Détails de l'Image Sélectionnée")

# Afficher le nom de l'image sélectionnée
st.write(f"Vous avez sélectionné : **{image_name}**")

# Exemple : Afficher d'autres informations liées à l'image
st.write("Voici des informations supplémentaires sur l'image sélectionnée.")