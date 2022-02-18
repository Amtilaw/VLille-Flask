import flask
from flask import Flask, request
from controllers import homeController
from models import stations

app = Flask(__name__)

def dico_render_view(_get, bdd):
    switcher = {
        "home": homeController.view(bdd),
        "page": homeController.view(bdd),
    }
    return switcher.get(_get, homeController.view(bdd))

@app.route("/")
def home():

    params_get = request.args

    repo_station = stations.get_all_stations()
    return dico_render_view(params_get, repo_station)

    

app.run(host="0.0.0.0", port=3000)