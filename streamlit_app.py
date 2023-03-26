
import streamlit as st
from pymongo import MongoClient

# Se connecter à la base de données MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['bdd']
collection = db['guide_des_arcs']

# Récupérer les données depuis la collection
donnees = collection.find()

# Afficher les données sous forme de tableau sur Streamlit
st.title('Liste des arcs de l\'attaque des titans')
st.table(donnees)

#   commnande a taper dans le terminal
#   cd C:\Users\User\Downloads
#   streamlit run streamlit_app.py
#   https://github.com/Tharse/Python.git
