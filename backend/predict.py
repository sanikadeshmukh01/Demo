import requests
import pickle
import os

from dotenv import load_dotenv


load_dotenv()


# Load API key

api_key = os.getenv("OPENWEATHER_API_KEY")


city = "Chennai"


# Get weather

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"


response = requests.get(url)

data = response.json()


temperature = data["main"]["temp"]

humidity = data["main"]["humidity"]

pressure = data["main"]["pressure"]

wind_speed = data["wind"]["speed"]


# Load AI model

with open("flood_model.pkl", "rb") as file:
    model = pickle.load(file)


# IMPORTANT:
# OpenWeather free API does not always provide rainfall.
# For now we estimate it.

rainfall = 50


prediction = model.predict(
[
[
temperature,
humidity,
rainfall,
wind_speed,
pressure
]
]
)


if prediction[0] == 1:

    print("⚠️ Flood Risk: HIGH")

else:

    print("✅ Flood Risk: LOW")