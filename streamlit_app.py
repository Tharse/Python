
import streamlit as st
from pymongo import MongoClient

# Connection bdd MongoDB et on selectionne la collection et la bdd
client = MongoClient('mongodb://localhost:27017/')
db = client['bdd']
collection = db['guide_des_arcs']

# Récupérer les données depuis la collection bdd
donnees = collection.find()

# Afficher les données sous forme de tableau sur Streamlit
st.title('Liste des arcs de l\'attaque des titans')
st.table(donnees)

#   commnande a taper dans le terminal
#   cd C:\Users\User\Downloads
#   streamlit run streamlit_app.py
#   https://github.com/Tharse/Python.git
