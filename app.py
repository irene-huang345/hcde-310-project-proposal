from flask import Flask, render_template, request
import requests
#from geopy.geocoders import Nominatim
from Main import gather_weather, gather_movies

app = Flask(__name__)

city_coords = {
    "New York": (40.7130466, -74.0072301),
    "Los Angeles": (34.06778, -118.24167),
    "Miami": (25.79, -80.32),
    "Seattle": (47.54548, -122.3147),
    "Chicago": (41.883229, -87.632398),
    "Philadelphia": (39.9511, -75.1656)
}

@app.route('/', methods=['GET', 'POST'])
def results():
    default_city = "New York"
    default_movies = gather_movies("Sunny")
    print(default_movies)

    if request.method == 'GET':
        #print("GET REQUEST")
        return render_template('index.html', movies = default_movies)

    if request.method == 'POST':
        #print("POST REQUEST")
        try:
            city_name = request.form.get('city_name')
            city_name = city_name.strip().title()

            if city_name in city_coords:
                latitude, longitude = city_coords[city_name]
                weather_type = gather_weather(latitude, longitude)
                print(weather_type)
                #print("CHECK ALL FOUR: ", city_name, latitude, longitude, weather_type)
                if weather_type:

                    movies = gather_movies(weather_type)

                   # print(f"\n\nweather type: {weather_type}")
                   # print(f"movies: {movies}")

                    return render_template('index.html', weather = weather_type, movies = movies,
                                           city_name = city_name)
                else:
                    return render_template('index.html', weather = None, movies = None,
                                           error = "data", city_name = city_name)

            else:
                return render_template('index.html', error = "City Name Not Found",
                                       city_name = city_name)

        except Exception as e:
            print(f"error: {e}")
            return "error exception: ", 404

    else:
        return render_template('index.html', movies = default_movies, city_name = default_city)


if __name__ == '__main__':
    app.run(debug=True)