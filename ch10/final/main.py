from nfl_weather_api import NFLWeatherAPI
from weather_api import OpenWeatherAPI

def main():
    nfl_api = NFLWeatherAPI()
    open_api = OpenWeatherAPI()

    games = [
        {"date": "2022-09-10", "home_team": "Atlanta Falcons", "away_team": "Philadelphia Eagles", "stadium": "Mercedes-Benz Stadium", "location": {"lat": 33.755388, "lon": -84.400487}},
        {"date": "2022-09-10", "home_team": "New Orleans Saints", "away_team": "Tampa Bay Buccaneers", "stadium": "Mercedes-Benz Superdome", "location": {"lat": 29.951066, "lon": -90.082174}},
        {"date": "2022-09-10", "home_team": "Minnesota Vikings", "away_team": "San Francisco 49ers", "stadium": "U.S. Bank Stadium", "location": {"lat": 44.974003, "lon": -93.259007}},
        {"date": "2022-09-11", "home_team": "Denver Broncos", "away_team": "Los Angeles Chargers", "stadium": "Sports Authority Field at Mile High", "location": {"lat": 39.743936, "lon": -105.020097}}
    ]

    for game in games:
        year, month, day = game["date"].split("-")

        nfl_data = nfl_api.get(year, month, day)
        open_data = open_api.get(game["location"]["lat"], game["location"]["lon"], "minutely,hourly")

        print(f"\nDate: {nfl_data['date']}")
        print(f"Home Team: {nfl_data['home_team']}")
        print(f"Away Team: {nfl_data['away_team']}")
        print(f"Stadium: {nfl_data['stadium']}")
        print(f"Weather: {open_data['current_temp']}°F with a high of {open_data['high_temp']}°")