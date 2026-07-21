from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import pickle
import os

from dotenv import load_dotenv

from resource_agent import allocate_resources
from communication_agent import generate_alert


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
load_dotenv()


api_key = os.getenv("OPENWEATHER_API_KEY")



@app.get("/")
def home():

    return {
        "message":"AI Disaster System Running"
    }



from fastapi import Query

@app.get("/disaster")
def disaster_status(city: str = Query(...)):





    # Get weather data

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
        [[
            temperature,
            humidity,
            rainfall,
            wind_speed,
            pressure
        ]]
    )


    risk = prediction[0]



    # Resource Agent

    resources = allocate_resources(risk)



    # Communication Agent

    alert = generate_alert(
        city,
        risk,
        resources
    )



    return {


        "city":city,


        "weather":{

            "temperature":temperature,

            "humidity":humidity,

            "wind_speed":wind_speed

        },


        "risk":risk,


        "resources":resources,


        "alert":alert

    }