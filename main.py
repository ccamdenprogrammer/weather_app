from geopy.geocoders import Nominatim
import tkinter
import geocoder
import requests
from pprint import pprint

def getWeatherData():
    api_key = '4ac9c0db8de88aef04819908732a03ab' #api key for open weather map
    
    
    g = geocoder.ip('me') #Gets lat and long of users current location utilizing geopy 
    lat, lng = g.latlng 
    latlng = (lat, lng)
    print(latlng)
    
    from geopy.geocoders import Nominatim # converts lat and long into a more readable city name
    geolocator = Nominatim(user_agent="http")
    location = geolocator.reverse(latlng)
    city = (location.raw.get('address').get('city')) #city is set to the current city

  
    base_URL = "http://api.openweathermap.org/data/2.5/weather?appid="+api_key+"&q="+city #requests the API to return data for users current city
    weather_data = requests.get(base_URL).json()

    pprint(weather_data) #prints weather data
   

getWeatherData()


    


    




