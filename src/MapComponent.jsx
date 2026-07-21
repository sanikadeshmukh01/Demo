import {
  MapContainer,
  TileLayer,
  Marker,
  Popup,
  useMap
} from "react-leaflet";

import "leaflet/dist/leaflet.css";


function ChangeMapView({ coords }) {

  const map = useMap();

  if (coords) {
    map.flyTo(coords, 10);
  }

  return null;
}


function MapComponent({ setCity }) {


  const handleCityClick = (city, coords) => {
    setCity(city);
  };


  return (

    <MapContainer
      center={[22.9734, 78.6569]}
      zoom={5}
      style={{
        height:"400px",
        width:"100%"
      }}
    >

      <TileLayer
        attribution="&copy; OpenStreetMap contributors"
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />


      <Marker
        position={[19.0760,72.8777]}
        eventHandlers={{
          click:(e)=>{
            handleCityClick(
              "Mumbai",
              [19.0760,72.8777]
            );
            e.target._map.flyTo(
              [19.0760,72.8777],
              10
            );
          }
        }}
      >
        <Popup>
          Mumbai
        </Popup>
      </Marker>



      <Marker
        position={[28.6139,77.2090]}
        eventHandlers={{
          click:(e)=>{
            handleCityClick(
              "Delhi",
              [28.6139,77.2090]
            );

            e.target._map.flyTo(
              [28.6139,77.2090],
              10
            );
          }
        }}
      >
        <Popup>
          Delhi
        </Popup>
      </Marker>




      <Marker
        position={[13.0827,80.2707]}
        eventHandlers={{
          click:(e)=>{
            handleCityClick(
              "Chennai",
              [13.0827,80.2707]
            );

            e.target._map.flyTo(
              [13.0827,80.2707],
              10
            );
          }
        }}
      >
        <Popup>
          Chennai
        </Popup>
      </Marker>


    </MapContainer>

  );
}


export default MapComponent;