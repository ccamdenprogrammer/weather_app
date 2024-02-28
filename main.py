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
    from geopy.geocoders import Nominatim # converts lat and long into a more readable city name
    geolocator = Nominatim(user_agent="http")
    location = geolocator.reverse(latlng)
    city = (location.raw.get('address').get('city')) #city is set to the current city

  
    base_URL = "http://api.openweathermap.org/data/2.5/weather?appid="+api_key+"&q="+city #requests the API to return data for users current city
    weather_data = requests.get(base_URL).json()

    temp_kelvin = weather_data['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_CF(temp_kelvin)
    feels_like_kelvin = weather_data['main']['feels_like']
    feels_like_celsius, feels_like_fahrenheit =kelvin_to_CF(feels_like_kelvin)
    description = weather_data['weather'][0]['description']

    print(f"The temperature in {city}: {temp_celsius:.2f} Degrees C / {temp_fahrenheit:.2f} Degrees F. \n")
    print(f"The temperature in {city} feels like: {feels_like_celsius:.2f} Degrees C / {feels_like_fahrenheit:.2f} Degrees F. \n")
    print(f"The weather in {city} is: {description}. \n")

def kelvin_to_CF(kelvin):
    celsius = kelvin-273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit
   

getWeatherData()


    


    




