
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

def insert_station_bdd(row_station):

    bdd = Bdd()
    try:  
        connection = bdd.get_connection()
        cursor = connection.cursor()
        # SQL 
        sql = "INSERT INTO `station`(`Id`, `nom`, `adresse`, `commune`, `etat`, `type`, `geo`, `nbPlaceDispo`, `nbVeloDispo`, `etatConnexion`, `localisation`, `date`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
        # Exécutez la requête (Execute Query).
        cursor.execute(sql, (row_station[0],row_station[1],row_station[2],row_station[3],row_station[4],row_station[5],row_station[6],row_station[7],row_station[8],row_station[9],row_station[10],row_station[11])) 
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
            all_row = []
            for row in cursor:
                all_row.append(row)
            return all_row
    finally:
        # Closez la connexion (Close connection).      
        bdd.close_connection()

def get_by_name_or_adress_stations(str):
    bdd = Bdd()
    try:  
        cursor = bdd.get_connection().cursor()
        # SQL 
        sql = "SELECT * FROM station WHERE nom LIKE '%"+ str +"%' OR adresse LIKE '%"+ str +"%'" 
        # Exécutez la requête (Execute Query).
        cursor.execute(sql)
        print ("cursor.description: ", cursor.description) 
        print() 
        all_row = []
        for row in cursor:
            print(row) 
            all_row.append(row)
        return all_row
    finally:
        # Closez la connexion (Close connection).      
        bdd.close_connection()

