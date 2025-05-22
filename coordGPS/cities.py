import json

cities = [
    "Le Mont-Saint-Michel, France", "Saint-Malo, France", "Bayeux, France", "Le Havre, France",
    "Rouen, France", "Paris, France", "Amiens, France", "Lille, France",
    "Strasbourg, France", "Château du Haut-Koenigsbourg, France", "Colmar, France", "Eguisheim, France",
    "Besançon, France", "Dijon, France", "Annecy, France", "Grenoble, France",
    "Lyon, France", "Gorges du Verdon, France", "Bormes-les-Mimosas, France", "Cassis, France",
    "Marseille, France", "Aix-en-Provence, France", "Avignon, France",
    "Uzes, France", "Nimes, France", "Aigues-Mortes, France", "Sainte-Marie de la Mer, France",
    "Collioure, France", "Carcassonne, France", "Ariège, France", "Toulouse, France",
    "Montauban, France", "Biarritz, France", "Bayonne, France", "La Rochelle, France"
]

file_name = "cities.json"

with open(file_name, "w", encoding="utf-8") as f:
    json.dump(cities, f, indent=4, ensure_ascii=False)

print(f" City list saved to {file_name}")
