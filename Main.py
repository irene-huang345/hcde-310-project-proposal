from flask import Flask
import requests

#any import statements here
#import json

#ChatGPT helped me with setting up my try and except errors to check for
def gather_weather(latitude, longitude):
    #user_agent = "(app, email)"

    try:
        weather_call = f"https://api.weather.gov/points/{latitude},{longitude}"
        results = requests.get(weather_call)

        results.raise_for_status()

        data = results.json()
        forecast = data['properties']['forecast']

        final = requests.get(forecast)

        cast_info = final.json()
        weather_type = cast_info['properties']['periods'][0]['shortForecast']

        return weather_type
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None

#ChatGPT helped me with the if/else branch in my try block because my code kept going into
# the except block so I thought it would help with debugging or any future errors I would run into
def gather_movies(weather_type):
    recs = {
        "Sunny": "Comedy",
        "Rain" : "Drama",
        "Cloudy" : "Action",
        "Snow" : "Romance",
        "Clear" : "Kids & Family",
        "Partly-Cloudy": "Crime",
    }

    genre = recs.get(weather_type.split()[0], "Comedy")

    try:
        omdb_url = f"https://www.omdbapi.com/?apikey=95839b7d&s={genre}&type=movie"
        omdb_results = requests.get(omdb_url)
        omdb_results.raise_for_status()
        data = omdb_results.json()

        if data.get('Response') == "True":
            return data.get('Search', [])
        else:
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []
    except ValueError as e:
        print(f"Error: {e}")
        return []

def main():
    latitude, longitude = 40.7128, -74.0060
    weather_type = gather_weather(latitude, longitude)

    if weather_type:
        print(f"Weather: {weather_type}")

        movies = gather_movies(weather_type)
        if movies:
            for movie in movies:
                print(movie)
        else:
            print("No movies found.")
    else:
        print("No data found")

if __name__ == "__main__":
    main()

