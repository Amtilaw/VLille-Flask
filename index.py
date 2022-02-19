from operator import mod
from typing import List
from flask import Flask, request
#Controller --> C'est où on fait des requêtes à la bdd et le code pour generer un template
from controllers import homeController
from controllers import installBddController
from controllers import searchController

app = Flask(__name__)
#Un dico qui lie le premier paramètre à un template
switcher = {
        "installBdd": installBddController,
        "home": homeController,
        "page": homeController,
        "search": searchController,
    }

def dico_render_view(first_get):
   
    return switcher.get(first_get, homeController).view() #Renvoi le template voulue sinon par defautl le template home


@app.route("/")
def home():

    params_get = request.args
    try:
        first_param = list(params_get.keys())[0]
    except IndexError:
        first_param = "none"

    #En fonction du nom du parametre renvoi un template
    return dico_render_view(first_param)

    

app.run(host="0.0.0.0", port=3000)