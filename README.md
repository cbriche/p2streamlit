# README - Mon Projet Streamlit

Bienvenue dans **Mon Projet Streamlit**, une application interactive développée avec **Streamlit**. Ce projet inclut des fonctionnalités pour afficher des images cliquables, naviguer entre plusieurs pages et effectuer des analyses basiques de données.

---

## 📂 Structure du projet

```
mon_projet_streamlit/
├── app.py                    # Page principale de l'application
├── pages/                    # Sous-pages (multi-pages)
│   ├── detail.py             # Page de détails
│   ├── reco.py               # Page de recommandations
│   └── img_clicable.py       # Page d'images cliquables
├── utils/                    # Fonctions utilitaires
│   └── data_loader.py        # Gestion et nettoyage des données
├── assets/                   # Fichiers statiques (CSS, images)
│   └── style.css             # Fichier CSS pour personnalisation
├── data/                     # Fichiers de données (CSV, JSON...)
├── .streamlit/               # Configuration de Streamlit
│   └── config.toml
├── requirements.txt          # Bibliothèques nécessaires
└── README.md                 # Documentation du projet
```

---

## 🛠️ Installation

### 1. Prérequis
- **Python 3.9** ou plus récent
- **Anaconda** (optionnel mais recommandé)
- **Git** installé sur votre machine

### 2. Configuration de l'environnement

1. **Clonez le projet** :
   ```bash
   git clone https://github.com/votre_nom_utilisateur/mon_projet_streamlit.git
   cd mon_projet_streamlit
   ```


## 🚀 Fonctionnalités principales

### 1. Navigation multi-pages
- **Page principale (`app.py`)** : Point d'entrée avec les principales fonctionnalités.
- **Pages secondaires** :
   - `detail.py` : Affiche les détails d'une sélection.
   - `reco.py` : Page de recommandations.
   - `img_clicable.py` : Présente une galerie d'images cliquables permettant de naviguer.

### 2. Images Cliquables
La page `img_clicable.py` affiche une grille d'images cliquables. En cliquant, vous êtes redirigé vers une page détaillée avec des informations supplémentaires.

### 3. Analyse des Données
Le module `data_loader.py` permet :
- De charger des fichiers CSV.
- De nettoyer et analyser les données pour une utilisation efficace dans l'application.

---

## 🎨 Personnalisation avec CSS

1. **Fichier CSS** : Le style est centralisé dans `assets/style.css`.
   Exemple de contenu :
   ```css
   .title {
       font-size: 36px;
       color: #4CAF50;
       text-align: center;
   }
   ```

2. **Chargement du CSS** : Utilisez une fonction dédiée dans `app.py` :
   ```python
   def load_css(file_path):
       with open(file_path) as f:
           st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

   load_css("assets/style.css")
   ```

---


## 👤 Auteurs

** Matine - Bénédicte - Guillaume - Corinne **

Pour toute question, n'hésitez pas à ouvrir une *issue* dans ce dépôt GitHub.

