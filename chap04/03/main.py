import os
import json
import requests
import math


WEATHER_API_KEY = os.environ.get("OPEN_WEATHER_API_KEY")

def geo_code(location):
    loc = location.split(",")[0]
    url = (
        f"http://api.openweathermap.org/geo/1.0/direct?q={loc}&appid={WEATHER_API_KEY}"
    )

    try:
        response = requests.get(url)
        response.raise_for_status()
        coordinates = response.json()
        lat = coordinates[0].get("lat")
        lon = coordinates[0].get("lon")
        return lat, lon

    except requests.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return None, None

def get_current_weather(location):
    lat, lon = geo_code(location)

    if lat is None or lon is None:
        print("Failed to get location coordinates.")
        return

    try:
        response = requests.get("https://api.openweathermap.org/data/2.5/weather", params={
            "lat": lat,
            "lon": lon,
            "units": "metric",
            "lang": "ja",
            "appid": WEATHER_API_KEY
        })
        response.raise_for_status()
        weather_data = response.json()
        current_temp = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]

        weather_info = {
            "location": location,
            "temperature": math.floor(current_temp),
            "forecast": description,
        }

        # make sure to convert to stringified json object
        return json.dumps(weather_info)

    except requests.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return

def main():
    print(get_current_weather("tokyo,JP"))


if __name__ == "__main__":
    main()