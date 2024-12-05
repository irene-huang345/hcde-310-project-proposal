from flask import Flask, render_template, request
import requests

from Main import gather_weather, gather_movies

app = Flask(__name__)

city_coords = {
    "New York": (40.78, 73.97),
    "Los Angeles": (34.06778, 118.24167),
    "Miami": (25.79, 80.32),
    "Seattle": (47.54548, 122.3147)
}

@app.route('/', methods=['GET', 'POST'])
def results():
    default = gather_movies("Sunny")

    if request.method == 'POST':
        try:
            city_name = request.form.get('city_name')
            city_name = city_name.strip().title()

            if city_name in city_coords:
                latitude, longitude = city_coords[city_name]
                weather_type = gather_weather(latitude, longitude)

                if weather_type:

                    movies = gather_movies(weather_type)

                    print(f"weather type: {weather_type}")
                    print(f"movies: {movies}")

                    return render_template('index.html', weather = weather_type, movies = movies)
                else:
                    return render_template('index.html', weather = None, movies = None, error = "data")

            else:
                return render_template('index.html', error = "City Name Not Found")


        except Exception as e:
            print(f"error: {e}")
            return "error exception: ", 404

    else:
        return render_template('index.html', movies =[])


if __name__ == '__main__':
    app.run(debug=True)