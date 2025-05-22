<h1 align="center">Jedha's ML Engineer Certificate</h1>
<h2 align="center">Bloc 1 : Build & Manage a Data Infrastructure</h2>

<p align="center"><strong>One Case Study :</strong></p>
<p align="center">Data Collection & Management : <em>Plan your trip with Kayak</em></p>

---

### Objectif du projet

L'équipe marketing de **Kayak** souhaite créer une application qui recommandera les **meilleures destinations et hôtels français** en fonction :

- de la météo prévue dans les 7 prochains jours  
- des meilleurs hôtels disponibles dans la région

---

### Données utilisées

- **35 villes françaises** issues de _OneWeekIn.com_  
- Données météo via **OpenWeatherMap API**  
- Coordonnées via **Nominatim API**  
- Hôtels scrappés depuis **Booking.com** avec **Scrapy** :
  - Nom, coordonnées, note, description, URL

---

### Pipeline ETL

1. **Extraction**
   - API météo (OpenWeather)
   - Booking.com via un spider **Scrapy**
2. **Nettoyage & enrichissement**
3. **Stockage**
   - `.csv` enrichi stocké sur **AWS S3**
4. **Chargement**
   - Données chargées dans une **base PostgreSQL (AWS RDS)**

---

### Visualisation des résultats

#### Carte 1 : Top 5 des villes météo

- Réalisée avec **Plotly Express**
- Affiche les villes les plus "ensoleillées"
- Utilise un **score météo personnalisé** basé sur température, humidité, pluie, etc.

#### Carte 2 : Top hôtels par ville (Streamlit)

- Interface **Streamlit** avec **Folium**
- Sélection d'une ville → affichage dynamique des meilleurs hôtels  
- Chaque hôtel contient :
  - Nom
  - Note
  - Description
  - 🔗 Lien vers Booking.com

---

### Technologies utilisées

| Outil / Tech       | Rôle                              |
|--------------------|-----------------------------------|
| Python             | Langage principal                 |
| Pandas             | Traitement de données             |
| Requests           | Appels API météo et géocodage     |
| Scrapy             | Scraping structuré Booking.com    |
| Plotly             | Carte des meilleures destinations |
| Folium             | Carte hôtelière dynamique         |
| Streamlit          | Application web interactive       |
| AWS S3             | Stockage des données brutes       |
| AWS RDS (Postgres) | Entrepôt de données SQL           |

---

### Livrables

- Un fichier `.csv` dans un bucket **AWS S3** contenant les données météo + hôtels enrichies  
- Une **base SQL PostgreSQL** (hébergée sur **AWS RDS**) contenant les mêmes données  
- Deux cartes interactives :
  - **Top 5 des destinations météo** (24/04/2025 au 30/04/2025)
  - **Top 20 hôtels** répartis sur 35 villes françaises

---

### Critères d’évaluation de l’infrastructure

- **Simplicité et cohérence du projet d'infrastructure**
- **Capacité de stockage suffisante pour un projet Big Data**
- **Optimisation des coûts liés à la collecte, au stockage et à l'exploitation des données**
- **Qualité des données extraites du Web vers le Data Lake (scraping, APIs)**
- **Accessibilité rapide et fiable des données depuis le Data Warehouse**
- **Robustesse et efficacité du pipeline ETL conçu**
- **Conformité du processus de collecte aux normes RGPD**, notamment sur :
  - la nature des données collectées
  - leur stockage et leur utilisation
  - la protection de la vie privée des utilisateurs

---
