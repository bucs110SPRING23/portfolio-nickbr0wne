import requests

class NFLWeatherAPI:
    def __init__(self):
        self.api_url = "https://www.nflweather.com/api/"

    def get(self, year, month, day):
        response = requests.get(f"{self.api_url}/{year}/{month}/{day}")
        data = response.json()

        processed_data = {
            "date": f"{month}/{day}/{year}",
            "home_team": data["home_team"],
            "away_team": data["away_team"],
            "stadium": data["stadium"],
            "weather": data["forecast"]
        }

        return processed_data
