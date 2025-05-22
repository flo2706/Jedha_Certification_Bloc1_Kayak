import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

df = pd.read_csv("hotels_weather_final_ter.csv", encoding="utf-8-sig")

# Drop hotels without rating or coordinates
df = df.dropna(subset=["hotel_rating", "hotel_latitude", "hotel_longitude"])

# Sidebar selection
cities = df["city_name"].unique()
selected_city = st.selectbox("Choose a city", sorted(cities))

# Filter top hotels (sorted by rating)
top_hotels = df[df["city_name"] == selected_city].sort_values(
    by="hotel_rating", ascending=False
).head(20)

# Display centered dynamic title
nb_hotels = len(top_hotels)
st.markdown(
    f"<h2 style='text-align: center;'>Top {nb_hotels} Hotels in {selected_city}</h2>",
    unsafe_allow_html=True
)

# Create map centered on the first hotel
map_center = [top_hotels.iloc[0]["hotel_latitude"], top_hotels.iloc[0]["hotel_longitude"]]
m = folium.Map(location=map_center, zoom_start=14, tiles="OpenStreetMap")

# Add markers
for _, row in top_hotels.iterrows():
    name = row["hotel_name"]
    rating = row["hotel_rating"]
    url = row["hotel_url"]
    desc = row.get("hotel_description", "No description available")

    popup_html = f"""
    <strong>{name}</strong><br>
    <em>Rating:</em> {rating}<br>
    <em>Description:</em><br> {desc[:300]}...<br>
    <a href="{url}" target="_blank">🔗 View on Booking</a>
    """
    folium.Marker(
        location=[row["hotel_latitude"], row["hotel_longitude"]],
        popup=folium.Popup(popup_html, max_width=300),
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# Display the map in Streamlit
st_folium(m, width=800, height=600)
