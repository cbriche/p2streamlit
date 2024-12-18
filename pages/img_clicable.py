import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Galerie d'Images", layout="wide")

# Fonction pour afficher des images cliquables
def display_clickable_images(images):
    num_cols = 4
    cols = st.columns(num_cols)

    for i, image in enumerate(images):
        image_name = f"Image_{i+1}"  # Nom de l'image
        with cols[i % num_cols]:
            # Créer un lien cliquable avec st.markdown et passer l'image en paramètre
            st.markdown(
                f"""
                <a href="/pages/reco?image_name={image_name}" target="_self">
                    <img src="{image}" alt="{image_name}" width="250" style="border-radius: 8px; margin-bottom: 10px;">
                </a>
                """,
                unsafe_allow_html=True
            )

# Liste des images
images_us_matine = [
    "https://media.themoviedb.org/t/p/w300_and_h450_bestv2/2dTrBuRlKiKR7xRNEIs1RHCq9J8.jpg",
    "https://media.themoviedb.org/t/p/w300_and_h450_bestv2/2dTrBuRlKiKR7xRNEIs1RHCq9J8.jpg",
    "https://media.themoviedb.org/t/p/w300_and_h450_bestv2/2dTrBuRlKiKR7xRNEIs1RHCq9J8.jpg",
    "https://media.themoviedb.org/t/p/w300_and_h450_bestv2/2dTrBuRlKiKR7xRNEIs1RHCq9J8.jpg"
]

# Titre
st.title("Galerie d'Images")

# Section avec images cliquables
st.subheader("US Matine")
display_clickable_images(images_us_matine)
