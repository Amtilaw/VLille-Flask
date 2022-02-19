from flask import render_template
from models import stations

def view():

    #Appelle la bdd qui renvoie toutes les stations
    repo_station = stations.get_all_stations()
    
    return render_template("home.html", stations = repo_station)
        