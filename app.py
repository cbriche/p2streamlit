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
st.title("Bienvenue dans mon app Streamlit sans CSS 🚀")
st.markdown('<h1 class="title">Bienvenue sur mon app Streamlit avec CSS</h1>', unsafe_allow_html=True)
st.write("Ceci est une application avec un style personnalisé.")

# Chargement de données (exemple)
uploaded_file = st.file_uploader("Upload un fichier CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Aperçu des données :")
    st.dataframe(df)

    # Exemple d'analyse simple
    st.subheader("Statistiques descriptives")
    st.write(df.describe())

import streamlit as st

if st.button("Home"):
    st.switch_page("app.py")
if st.button("Reco"):
    st.switch_page("pages/reco.py")
if st.button("detail"):
    st.switch_page("pages/detail.py")
    
 # Créer une selectbox pour capturer le choix de l'utilisateur
option = st.selectbox(
    "Choisissez une option :",
    ["Option 1", "Option 2", "Option 3"]
)

# Stocker le choix dans st.session_state
st.session_state["selected_option"] = option

# Bouton pour aller vers une autre page
if st.button("Aller a reco"):
    st.switch_page("pages/reco.py")  # Redirige vers la page 1   