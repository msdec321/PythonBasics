#!/usr/bin/python3

#This is the weather data fetcher script.
#This script downloads JSON weather data from OpenWeatherMap.org, converts the data to a Python data structure and then prints the weather description and temperature for today.

import requests, json, sys
from pprint import pprint

def KtoF(K):
    return (K-273.15)*(9./5.)+32.

if len(sys.argv)<2:
    print('Error: Expected city')
    sys.exit()

location = ' '.join(sys.argv[1:])  #If city has a space (ex. San Francisco)
APPID = 'b4489d070134143e227eb242231d4bdc'

url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&APPID={APPID}'#b4489d070134143e227eb242231d4bdc
response = requests.get(url)
response.raise_for_status()

weatherJSON = json.loads(response.text)

print(f'Current weather in {location}: ')
print(f"{weatherJSON['weather'][0]['main']}-{weatherJSON['weather'][0]['description']}, temp: {round(KtoF(weatherJSON['main']['temp']),1)}")
