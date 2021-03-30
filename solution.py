import geocoder
import requests
from secrets import API_KEY

API_BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

destinations = [
    "Space Needle",
    "Crater Lake",
    "Golden Gate Bridge",
    "Yosemite National Park",
    "Las Vegas, Nevada",
    "Grand Canyon National Park",
    "Aspen, Colorado",
    "Mount Rushmore",
    "Yellowstone National Park",
    "Sandpoint, Idaho",
    "Banff National Park",
    "Capilano Suspension Bridge"
]

for place in destinations:
    lat, lng = geocoder.arcgis(place).latlng
    full_api_url = (f"{API_BASE_URL}?lat={lat}&lon={lng}&appid={API_KEY}")
    result = requests.request('GET', full_api_url).json()
    weather = result["weather"][0]["description"]
    kelvin = result["main"]["temp"]
    temperature = (kelvin - 273.15) * 1.8 + 32 
    temperature = "{0:.1f}".format(temperature)
    
    
    print(f"{place} is located at ({lat}, {lng})")
    print(f"At {place} right now, we are experiencing {weather} with a temperature of {temperature:}° F \n")
