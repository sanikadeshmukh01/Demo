import requests
from dotenv import load_dotenv
import os
import sqlite3


load_dotenv()


api_key = os.getenv("OPENWEATHER_API_KEY")

city = "Chennai"


url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"


response = requests.get(url)

data = response.json()


city_name = data["name"]

temperature = data["main"]["temp"]

humidity = data["main"]["humidity"]

pressure = data["main"]["pressure"]

wind_speed = data["wind"]["speed"]

weather = data["weather"][0]["description"]


weather_data = {

    "city": city_name,
    "temperature": temperature,
    "humidity": humidity,
    "pressure": pressure,
    "wind_speed": wind_speed,
    "weather": weather

}


print(weather_data)



# DATABASE PART

connection = sqlite3.connect("weather.db")

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS weather_data(

id INTEGER PRIMARY KEY AUTOINCREMENT,
city TEXT,
temperature REAL,
humidity INTEGER,
pressure INTEGER,
wind_speed REAL,
weather TEXT

)
""")


cursor.execute("""
INSERT INTO weather_data
(city, temperature, humidity, pressure, wind_speed, weather)

VALUES (?, ?, ?, ?, ?, ?)

""",
(
weather_data["city"],
weather_data["temperature"],
weather_data["humidity"],
weather_data["pressure"],
weather_data["wind_speed"],
weather_data["weather"]
))


connection.commit()

connection.close()


print("Weather data stored successfully!")
# Check stored data

connection = sqlite3.connect("weather.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM weather_data")

rows = cursor.fetchall()

print(rows)

connection.close()