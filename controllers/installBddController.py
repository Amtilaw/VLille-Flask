import csv
from flask import redirect
from models import stations

def view():

    #Créer la table stations et charge les données du csv
    stations.create_table_station()
    parse_file() 

    return redirect('/')

def parse_file():
    rows = []

    with open('vlille-realtime.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            stations.insert_station_bdd(row)                                        #Insertion d'une table station
            rows.append(row)
        return rows
        