
from models.bdd import Bdd

def create_table_station():
    bdd = Bdd()
    try:  
        connection = bdd.get_connection()
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE station (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), adresse VARCHAR(255),commune VARCHAR(255), etat VARCHAR(255), type VARCHAR(255), geo VARCHAR(255), nbPlaceDispo INT, nbVeloDispo INT, etatConnexion VARCHAR(255), localisation VARCHAR(255), date VARCHAR(255))")
        # SQL 
    finally:
        # Closez la connexion (Close connection).      
        bdd.close_connection()

def insert_station_bdd(rowStation):

    bdd = Bdd()
    try:  
        connection = bdd.get_connection()
        cursor = connection.cursor()
        # SQL 
        sql = "INSERT INTO `station`(`Id`, `nom`, `adresse`, `commune`, `etat`, `type`, `geo`, `nbPlaceDispo`, `nbVeloDispo`, `etatConnexion`, `localisation`, `date`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
        # Exécutez la requête (Execute Query).
        cursor.execute(sql, (rowStation[0],rowStation[1],rowStation[2],rowStation[3],rowStation[4],rowStation[5],rowStation[6],rowStation[7],rowStation[8],rowStation[9],rowStation[10],rowStation[11])) 
        print ("cursor.description: ", cursor.description) 
        connection.commit()
          
    finally:
        # Closez la connexion (Close connection).      
        bdd.close_connection()

def get_all_stations():

    bdd = Bdd()

    try: 
        connection = bdd.get_connection()
        with connection.cursor() as cursor: 
            # SQL 
            sql = "SELECT * FROM `station` WHERE 1" 
            # Exécutez la requête (Execute Query).
            cursor.execute(sql) 
            allRow = []
            for row in cursor:
                allRow.append(row)
            return allRow
    finally:
        # Closez la connexion (Close connection).      
        bdd.close_connection()

