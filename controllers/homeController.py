import imp
from flask import render_template


def view(bdd):

    station_model = bdd
    return render_template("home.html", stations = station_model)
        
