import { useEffect, useState } from "react";
import "./App.css";
import MapComponent from "./MapComponent";


function App() {

  const [data, setData] = useState(null);
  const [city, setCity] = useState("Mumbai");


  const API_URL = import.meta.env.VITE_API_URL;


  console.log("Current City:", city);


  useEffect(() => {

    console.log("Fetching data for:", city);


    fetch(`${API_URL}/disaster?city=${city}`)

      .then((res) => res.json())

      .then((result) => {
        console.log(result);
        setData(result);
      })

      .catch((err) => {
        console.log(err);
      });


  }, [city]);



  if (!data) {

    return (
      <h2 className="loading">
        Loading AI Disaster System...
      </h2>
    );

  }



  return (

    <div className="dashboard">


      <h1>
        🚨 AI Disaster Response Dashboard
      </h1>



      <div className="card">

        <MapComponent 
          setCity={setCity}
        />

      </div>




      <div style={{marginBottom:"20px"}}>


        <button
          onClick={()=>setCity("Mumbai")}
        >
          Mumbai
        </button>



        <button

          onClick={()=>setCity("Delhi")}

          style={{marginLeft:"10px"}}

        >
          Delhi
        </button>




        <button

          onClick={()=>setCity("Chennai")}

          style={{marginLeft:"10px"}}

        >
          Chennai
        </button>


      </div>





      <div className="row">


        <div className="card">

          <h2>
            🌍 Location
          </h2>

          <p>
            {data.city}
          </p>

        </div>




        <div className="card">


          <h2>
            ⚠️ Risk Level
          </h2>


          <h1

          className={
            data.risk === "HIGH"
            ? "high"
            : data.risk === "MEDIUM"
            ? "medium"
            : "low"
          }

          >

          {data.risk}

          </h1>


        </div>


      </div>





      <div className="card">


        <h2>
          🌦 Weather
        </h2>


        <p>
          🌡 Temperature : {data.weather.temperature} °C
        </p>


        <p>
          💧 Humidity : {data.weather.humidity}%
        </p>


        <p>
          🌬 Wind Speed : {data.weather.wind_speed} m/s
        </p>


      </div>






      <div className="card">


        <h2>
          🚑 Resources
        </h2>


        <p>
          Ambulances : {data.resources.ambulances}
        </p>


        <p>
          Rescue Teams : {data.resources.rescue_teams}
        </p>


        <p>
          Food Packets : {data.resources.food_packets}
        </p>


        <p>
          Water Supply : {data.resources.water_supply}
        </p>


      </div>






      <div className="card">


        <h2>
          📢 Emergency Alert
        </h2>


        <pre>
          {data.alert}
        </pre>


      </div>



    </div>

  );

}


export default App;