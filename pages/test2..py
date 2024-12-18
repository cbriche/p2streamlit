import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Galerie d'Images", layout="wide")

# Fonction pour afficher les images en 4 colonnes
def display_image_columns(images):
    num_cols = 4  # Nombre de colonnes
    cols = st.columns(num_cols)  # Crée les colonnes

    for i, image in enumerate(images):
        with cols[i % num_cols]:  # Place l'image dans la bonne colonne
            st.image(image, caption=f"Image {i+1}", width=150)

# Titre principal
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Galerie d'Images</h1>", unsafe_allow_html=True)

# Section US Matine
st.subheader("US Matine")
images_us_matine = [
    "https://media.themoviedb.org/t/p/w300_and_h450_bestv2/2dTrBuRlKiKR7xRNEIs1RHCq9J8.jpg",
    "https://media.themoviedb.org/t/p/w300_and_h450_bestv2/2dTrBuRlKiKR7xRNEIs1RHCq9J8.jpg",
    "https://media.themoviedb.org/t/p/w300_and_h450_bestv2/2dTrBuRlKiKR7xRNEIs1RHCq9J8.jpg",
    "https://media.themoviedb.org/t/p/w300_and_h450_bestv2/2dTrBuRlKiKR7xRNEIs1RHCq9J8.jpg"
]
display_image_columns(images_us_matine)

# Section US Guillaume
st.subheader("US Guillaume")
images_us_guillaume = images_us_matine  # Exemple identique pour tester
display_image_columns(images_us_guillaume)

# Section FR Bene
st.subheader("FR Bene")
images_fr_bene = images_us_matine  # Exemple identique pour tester
display_image_columns(images_fr_bene)

# Section FR Corinne
st.subheader("FR Corinne")
images_fr_corinne = images_us_matine  # Exemple identique pour tester
display_image_columns(images_fr_corinne)
