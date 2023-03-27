# TP PYTHON - Thangarajah Tharsegan

![enter image description here](https://cdn.hackersandslackers.com/2020/11/beautifulsoup.jpg)


# Le premier script

Un scrapper/api générant des données sous forme de tableaux

    import  matplotlib.pyplot  as  plt
    from  bs4  import  BeautifulSoup  as  bs
    pip install requests
    pip install lxml

    
    

Voici le site qu'on va scrapper : https://attaque-des-titans.fandom.com/fr/wiki/Guide_des_Arcs

# Deuxième script
un script capable d’ingérer les données dans la bdd

Tout d'abord on installe MongoDB Compass sur notre systeme et on l'ouvre

    pip install pymongo
    import pymongo
    db.list_collection_names()
Une fois que les données sont ingérer on se connecte a notre base de donnée et on se place dans la bonne collection : ![enter image description here](https://drive.google.com/file/d/1wYkMycsxhnkfN5yGnwi3plsYwVqcD2Z7/view?usp=share_link)




# Troisième Script
Un script capable d’interroger la base de donnée pour afficher les données sous forme de tableau sur un Dashboard de type streamlit

Tout d'abord on installe Streamlit sur notre systeme.
On creer un fichier .py : 


   
    client = MongoClient('mongodb://localhost:27017/')
    db = client['bdd']
    collection = db['guide_des_arcs']
    donnees = collection.find()
    st.title('Liste des arcs de l\'attaque des titans')
    st.table(donnees)
Puis on ouvre le terminal et on se place dans le repertoire du fichier .py et on lance la commande : 

    streamlit run streamlit_app.py
ici notre fichier s'appelle streamlit_app

Une fois la commande lancé le fichier s'ouvre sur un navigateur web :
![enter image description here](https://drive.google.com/file/d/1KcXiU6MxVK_5jGdABAGV9mfXlJv-xfoG/view?usp=share_link) 
