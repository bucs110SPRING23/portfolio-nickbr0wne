import requests

class OpenWeatherAPI:
    def __init__(self):
        self.api_url = "https://api.openweathermap.org/data/2.5/onecall"
        self.api_key = "ba9bf23047200c326065dc1948715ca3"

    def get(self, lat, lon, exclude):
        params = {
            "lat": lat,
            "lon": lon,
            "exclude": exclude,
            "appid": self.api_key
        }

        response = requests.get(self.api_url, params=params)
        data = response.json()

        processed_data = {
            "current_temp": data["current"]["temp"],
            "high_temp": data["daily"][0]["temp"]["max"],
            "low_temp": data["daily"][0]["temp"]["min"]
        }

        return processed_data
