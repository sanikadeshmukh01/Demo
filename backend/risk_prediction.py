import requests
import pickle
import os

from dotenv import load_dotenv


load_dotenv()


api_key = os.getenv("OPENWEATHER_API_KEY")


city = "Chennai"


url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"


response = requests.get(url)

data = response.json()


temperature = data["main"]["temp"]

humidity = data["main"]["humidity"]

pressure = data["main"]["pressure"]

wind_speed = data["wind"]["speed"]


# Temporary rainfall value
# Later we connect rainfall API

rainfall = 150



# Load AI model

with open("risk_model.pkl","rb") as file:
    model = pickle.load(file)



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


risk = prediction[0]


print("----------------------")
print("Disaster Monitoring")
print("----------------------")

print("City:", city)

print("Temperature:",temperature)

print("Humidity:",humidity)

print("Rainfall:",rainfall)

print("Wind:",wind_speed)


print("----------------------")

print("AI Risk Level:",risk)

print("----------------------")