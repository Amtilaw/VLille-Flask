from operator import mod
from typing import List
import flask
from flask import Flask, request
#Controller --> C'est où on fait des requêtes à la bdd et le code pour generer un template
from controllers import homeController
from controllers import installBddController

app = Flask(__name__)
#Un dico qui lie les paramètres d'une url à un template
switcher = {
        "installBdd": installBddController,
        "home": homeController,
        "page": homeController,
    }

def dico_render_view(_gets, firstGet):
   
    return switcher.get(firstGet, homeController).view()


@app.route("/")
def home():

    params_get = request.args
    try:
        first_param = list(params_get.keys())[0]
    except IndexError:
        first_param = "none"

    #En fonction du nom du parametre renvoi un template
    return dico_render_view(params_get, first_param)

    

app.run(host="0.0.0.0", port=3000)