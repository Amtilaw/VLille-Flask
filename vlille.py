import flask
from flask import Flask, render_template, request, jsonify, redirect, json, url_for
import csv
import pymysql.cursors 

app = Flask(__name__)


#TODO
#Populate la bdd avec l'api sur la route ApiGetVlille
#Affiche sur une map la localisation dans les détailles
#Nav bar --> html/css
#Recherche stations avec un champ
#Liste stations avec pagination

API_URL = "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=&rows=20&facet=libelle&facet=nom&facet=commune&facet=etat&facet=type&facet=etatconnexion"

connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',                             
                                db='pythonVlille',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor) 
def connectionBdd():
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',                             
                                db='pythonVlille',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor) 
    return connection

def parseFile():
    rows = []

    with open('vlille-realtime.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            newRow = row
            insertStationBdd(newRow)
            rows.append(newRow)
        connection.close()
        return rows


@app.route("/")
def home():
    if "station" in request.args:
        stations = getByNameOrAdressStations(request.args["station"])
        return render_template("index.html", stations= stations)
    if "search" in request.args:
        return request.args["search"]
    if "id" in request.args:
        return request.args["id"]
    return "hello"


@app.route(rule="/form", methods=["GET"])
def create():
    return "FORM"


@app.route("/listeStations")
def renderStations():
    allStation = getAllStations()
    return render_template("index.html", stations=allStation)

@app.route("/createDb")
def createDb():
    #bddConnection()
    row = parseFile()
    # print(row)
    return "remplissage de la table stations dans la bdd pythonVlille"

def insertStationBdd(rowStation):
    try:  
        cursor = connection.cursor()
        # SQL 
        sql = "INSERT INTO `station`(`Id`, `nom`, `adresse`, `commune`, `etat`, `type`, `geo`, `nbPlaceDispo`, `nbVeloDispo`, `etatConnexion`, `loaclisation`, `date`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
        # Exécutez la requête (Execute Query).
        cursor.execute(sql, (rowStation[0],rowStation[1],rowStation[2],rowStation[3],rowStation[4],rowStation[5],rowStation[6],rowStation[7],rowStation[8],rowStation[9],rowStation[10],rowStation[11])) 
        print ("cursor.description: ", cursor.description) 
        connection.commit()
          
    finally:
        # Closez la connexion (Close connection).      
        print("yes")

def getAllStations():
    try:  
        with connection.cursor() as cursor: 
            # SQL 
            sql = "SELECT * FROM `station` WHERE 1" 
            # Exécutez la requête (Execute Query).
            cursor.execute(sql) 
            print ("cursor.description: ", cursor.description) 
            print() 
            allRow = []
            for row in cursor:
                print(row) 
                allRow.append(row)
            return allRow
    finally:
        # Closez la connexion (Close connection).      
        connection.close()

def getByNameOrAdressStations(str):
    connexion = connectionBdd()
    try:  
        cursor = connexion.cursor()
        # SQL 
        sql = "SELECT * FROM station WHERE nom LIKE '%"+ str +"%' OR adresse LIKE '%"+ str +"%'" 
        # Exécutez la requête (Execute Query).
        cursor.execute(sql)
        print ("cursor.description: ", cursor.description) 
        print() 
        allRow = []
        for row in cursor:
            print(row) 
            allRow.append(row)
        return allRow
    finally:
        # Closez la connexion (Close connection).      
        connexion.close()

app.run(host="0.0.0.0", port=3000)

