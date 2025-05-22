# Jedha's ML Engineer certificate - Bloc 1 : Build & Manage a Data Infrastructure 
<h1 align="center">Plan your trip with Kaya</h1>

---

## Objectif du projet

L'équipe marketing de **Kayak** souhaite créer une application qui recommandera les **meilleures destinations et hôtels français** en fonction :

- de la météo prévue dans les 7 prochains jours
- des meilleurs hôtels de la région disponibles

---

## Données utilisées

- **35 villes françaises** issues de _OneWeekIn.com_
- Données météo via **OpenWeatherMap API**
- Coordonnées via **Nominatim API**
- Hôtels scrappés depuis **Booking.com** avec **Scrapy** :
  - Nom, coordonnées, note, description, URL

---

## Pipeline ETL

1. **Extraction**
   - API météo (OpenWeather)
   - Booking.com via un spider **Scrapy**
2. **Nettoyage & enrichissement**
3. **Stockage**
   - `.csv` enrichi stocké sur **AWS S3**
4. **Chargement**
   - Données chargées dans une **base PostgreSQL (AWS RDS)**

---

## Visualisation des résultats

### Carte 1 : Top 5 des villes météo

- Créée avec **Plotly Express**
- Affiche les villes les plus "ensoleillées"
- Utilise un **score météo personnalisé** basé sur température, humidité, pluie, etc.

### Carte 2 : Top hôtels par ville (Streamlit)

- Interface **Streamlit** avec **Folium**
- Sélection d'une ville → affichage des meilleurs hôtels (avec note disponible)
- Chaque hôtel contient :
  - Nom
  - Note
  - Description
  - 🔗 Lien vers Booking.com
- Une **tableau complémentaire** liste les hôtels avec liens cliquables

---

## Technologies utilisées

| Outil / Tech       | Rôle                              |
| ------------------ | --------------------------------- |
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

## Livrables

- `hotels_weather_final.csv` : données enrichies
- `app.py` : application Streamlit avec carte des hôtels
- `scrapy_spider.py` : spider pour Booking.com (hôtels)
- `ETL scripts` : extraction, nettoyage, upload vers S3

---
