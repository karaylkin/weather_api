from weather_api.owm_key import owm_api_key
import json
import requests

def get_weather_data(place, api_key=None):
  r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}')

  if r.status_code == 200:
    weather_data= r.json()
    place = f'Город: {weather_data["name"]}'
    country = f'Страна: {weather_data["sys"]["country"]}'
    lon = f'Долгота: {weather_data["coord"]["lon"]}'
    lat = f'Широта: {weather_data["coord"]["lat"]}'
    time_zone = weather_data['timezone']
    utc_offset = time_zone / 3600
    time = f'Временная зона: UTC{utc_offset:+.1f}'
    temp = f'Температура: {round(weather_data["main"]["temp"] - 273.15,2)}°C'
    feelslike = f'Ощущается как: {round(weather_data["main"]["feels_like"] - 273.15,2 )}°C'

    result = "\n".join([place, country, lon, lat, time, temp, feelslike])
    return result

  else:
    print(f"Error: {r.status_code}")

if __name__ == '__main__':
  get_weather_data('Moscow', api_key=owm_api_key)
