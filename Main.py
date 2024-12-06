from flask import Flask
import requests
import os
from dotenv import load_dotenv

load_dotenv()
omdb_api_key = os.getenv("OMDB_API_KEY")


#ChatGPT helped me with setting up my try and except errors to check for
def gather_weather(latitude, longitude):
    #user_agent = "(app, email)"

    try:
        weather_call = f"https://api.weather.gov/points/{latitude},{longitude}"
        print(f"weather data for: {latitude}, {longitude}")

        results = requests.get(weather_call)
        results.raise_for_status()


        data = results.json()
        print("data",data)

        forecast = data['properties']['forecast']
        print("forecast", forecast)

        final = requests.get(forecast)
        final.raise_for_status()

        cast_info = final.json()
        print("cast_info",cast_info)


        if 'properties' in cast_info and 'periods' in cast_info['properties']:
            weather_type = cast_info['properties']['periods'][0]['shortForecast']
            print(weather_type)
            return weather_type
        else:
            print("error, no periods found")
            return None

        #print("weather", weather_type)

       # return weather_type
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
        omdb_url = f"https://www.omdbapi.com/?apikey={omdb_api_key}&s={genre}&type=movie"
        print(f"OMDB URL: {omdb_url}")
        omdb_results = requests.get(omdb_url)
        omdb_results.raise_for_status()
        data = omdb_results.json()


        if data.get('Response') == "True":
            movies_to_display = data.get('Search', [])
            # print(movies_to_display)
            return movies_to_display
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


