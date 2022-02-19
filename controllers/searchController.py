from flask import render_template
from models import stations
from flask import request

def view():

    #Appelle la bdd qui renvoie toutes les stations
    search = request.args["search"]
    repo_station = stations.get_by_name_or_adress_stations(search)

    api_key = "AIzaSyAd4I7RM-VAkaZEF1Hr2GBC5P1g9iO-vU4"
    
    return render_template("home.html", stations = repo_station, api_key = api_key)
        