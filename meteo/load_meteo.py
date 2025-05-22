import requests
import csv
import json
from datetime import datetime, UTC
import os
from dotenv import load_dotenv

# Configuration
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
COORDS_FILE = "coordinates.json"
OUTPUT_CSV = "weather_7_day_forecast.csv"

# Load city coordinates from JSON file 
try:
    with open(COORDS_FILE, "r", encoding="utf-8") as file:
        cities = json.load(file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error loading coordinates: {e}")
    exit()

# Open CSV file for writing forecast data 
with open(OUTPUT_CSV, mode='w', newline='', encoding='utf-8') as csvfile:
    fieldnames = [
        'city', 'date', 'temp_min', 'temp_max', 'temp_feels_like', 'humidity', 'pressure',
        'wind_speed', 'wind_gust', 'wind_deg', 'clouds', 'uvi', 'dew_point', 'pop',
        'sunrise', 'sunset', 'moon_phase', 'conditions'
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Loop through each city 
    for city_name, coords in cities.items():
        try:
            lat = float(coords["latitude"])
            lon = float(coords["longitude"])

            # OpenWeatherMap One Call 3.0 API endpoint
            url = (
                f"https://api.openweathermap.org/data/3.0/onecall"
                f"?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=en"
            )

            response = requests.get(url)
            data = response.json()

            if response.status_code == 200 and "daily" in data:
                for day in data["daily"][:7]:  # Limit to 7 days
                    date = datetime.fromtimestamp(day["dt"], UTC).strftime('%Y-%m-%d')
                    sunrise = datetime.fromtimestamp(day["sunrise"], UTC).strftime('%H:%M:%S')
                    sunset = datetime.fromtimestamp(day["sunset"], UTC).strftime('%H:%M:%S')


                    row = {
                        'city': city_name,
                        'date': date,
                        'temp_min': day["temp"]["min"],
                        'temp_max': day["temp"]["max"],
                        'temp_feels_like': day["feels_like"]["day"],
                        'humidity': day["humidity"],
                        'pressure': day["pressure"],
                        'wind_speed': day["wind_speed"],
                        'wind_gust': day.get("wind_gust", "N/A"),
                        'wind_deg': day["wind_deg"],
                        'clouds': day["clouds"],
                        'uvi': day["uvi"],
                        'dew_point': day["dew_point"],
                        'pop': day["pop"], 
                        'sunrise': sunrise,
                        'sunset': sunset,
                        'moon_phase': day["moon_phase"],
                        'conditions': day["weather"][0]["description"]
                    }

                    writer.writerow(row)

            else:
                print(f"API error for {city_name}: {data}")

        except Exception as e:
            print(f"Error for {city_name}: {e}")

print(f"Weather data successfully saved to {OUTPUT_CSV}")
