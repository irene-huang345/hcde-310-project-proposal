from flask import flask
import requests

#any import statements here
#import json



#Set up National Weather Service API
# set up the OMDB API key
OMDB_API_KEY = ("https://urldefense.com/v3/__http://www.omdbapi.com/?i=tt3896198&apikey=95839b7d__;!!K-Hz7m0Vt54!"
                "kKaRSQH0DdX)pesd2Tey4Fk5L8aE-wiowfu5R1bnu_2SfeQFXbRDt1o83Aam21cgSZL8MkMKbqWr9bMZKmC-I$"

NWS_BASE_URL = "https://api.weather.gov/"

#define a function here "gather movies"
# call the omdb api here
##retrieve movies associated by genre
#Sunny forecast: comedies, Musicals
#Rainy forecast: Drama, horror, Action

#implement an if/else branch
# if the weather condition can be mapped to a movie
    #add the movie to a list
    #return the list
#else:
    #return an empty list


#define a function here "gather weather"
# need to use latitiude and longitude as parameters for this function
#set  up "try"
#Use "User-Agent: (myweatherapp.com, contact@myweatherapp.com) to set up API
# set up "except"
# implement any errors here that may come up in the code if data retrieval isn't successful

if __name__ = '__main__':
     app.run(debug=True)
