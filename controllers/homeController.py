from flask import render_template
from models import stations

def view():

    #Appelle la bdd qui renvoie toutes les stations
    repo_station = stations.get_all_stations()
    api_key = "AIzaSyAd4I7RM-VAkaZEF1Hr2GBC5P1g9iO-vU4"
    
    return render_template("home.html", stations = repo_station, api_key = api_key)
        