<h1 align="center">Jedha's ML Engineer Certificate</h1>
<h2 align="center">Bloc 1: Build & Manage a Data Infrastructure</h2>

<p align="center"><strong>One Case Study:</strong></p>
<p align="center">Data Collection & Management – <em>Plan Your Trip with Kayak</em> 🧳</p>
<br>

---

### Contexte de l'entreprise

**Kayak** est un moteur de recherche de voyages fondé en 2004 par Steve Hafner et Paul M. English.  
Il permet aux utilisateurs de comparer des offres de vols, hôtels, locations de voiture, et plus encore, pour planifier leur voyage au meilleur prix.

Depuis son rachat par **Booking Holdings**, Kayak fait partie d’un groupe qui possède également :
- Booking.com  
- Priceline  
- Agoda  
- OpenTable  
- Rentalcars.com

Avec plus de **300 millions de dollars de revenus par an**, Kayak est présent dans presque tous les pays et langues du monde, offrant une plateforme robuste pour l’organisation de voyages.

---

### Objectif du projet

Suite à une étude marketing, l’équipe de **Kayak** a constaté que :

- **70 % des utilisateurs** aimeraient obtenir davantage d’informations utiles sur leur destination.
- Les utilisateurs font davantage confiance à des données venant **de la marque elle-même**, plutôt qu'à des sites tiers.

> L’objectif du projet est donc de créer une **application intelligente** qui recommande les **meilleures destinations et hôtels** français, à partir de **données météo et hôtelières en temps réel.**

---

### Données utilisées

- **35 villes françaises** issues de _OneWeekIn.com_  
- Données météo via **OpenWeatherMap API**  
- Coordonnées géographiques via **Nominatim API**  
- Hôtels scrappés depuis **Booking.com** avec **Scrapy** :
  - Nom, coordonnées, note, description, URL

---

### Pipeline ETL

1. **Extraction**
   - API météo (OpenWeather)
   - Scraping des hôtels avec **Scrapy**
2. **Nettoyage & enrichissement**
3. **Stockage**
   - Fichier `.csv` enrichi sur **AWS S3**
4. **Chargement**
   - Données importées dans **PostgreSQL (AWS RDS)**

---

### Visualisation des résultats

#### Carte 1 : Top 5 des villes météo

- Réalisée avec **Plotly Express**
- Affiche les villes ayant le meilleur score météo
- Score basé sur température, humidité, pluie, etc.

#### Carte 2 : Top hôtels par ville

- Interface **Streamlit** avec **Folium**
- Sélection de ville → affichage des meilleurs hôtels disponibles
- Chaque hôtel inclut :
  - Nom
  - Note
  - Description
  - 🔗 Lien vers Booking.com

---

### Technologies utilisées

| Outil / Tech       | Rôle                              |
|--------------------|-----------------------------------|
| Python             | Langage principal                 |
| Pandas             | Manipulation des données          |
| Requests           | Appels API (météo, géocodage)     |
| Scrapy             | Scraping structuré Booking.com    |
| Plotly             | Visualisation météo               |
| Folium             | Carte hôtelière interactive       |
| Streamlit          | Interface utilisateur web         |
| AWS S3             | Stockage de données brutes        |
| AWS RDS (Postgres) | Base de données relationnelle     |

---

### Livrables

- Un fichier `.csv` enrichi disponible sur un bucket **AWS S3**
- Une base PostgreSQL contenant les mêmes données nettoyées
- Deux cartes :
  - **Top 5 des destinations météo** (24/04/2025 - 30/04/2025)
  - **Top 20 hôtels** pour 35 villes analysées

---

### Critères d’évaluation de l’infrastructure

- **Simplicité et clarté du projet d'infrastructure**
- **Capacité de stockage suffisante pour des volumes importants (Big Data ready)**
- **Coût maîtrisé des solutions déployées (stockage, calcul, API)**
- **Qualité des données extraites (exhaustivité, précision, structure)**
- **Accessibilité et rapidité d’accès aux données stockées**
- **Fiabilité du pipeline ETL mis en place**
- **Conformité RGPD sur les données utilisateur collectées**

---
