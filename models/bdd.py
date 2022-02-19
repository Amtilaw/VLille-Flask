import pymysql.cursors 
from dotenv import dotenv_values
config = dotenv_values(".env")

#Utilisation du fichier .env pour les variables d'environnement

USER = config.get("USER")
PASSWORD = config.get("PASSWORD")
DB_NAME = config.get("DB_NAME")
HOST = config.get("HOST")

class Bdd:
   
    def __init__(self): 
        self.connection = pymysql.connect(host=HOST,
                                        user=USER,
                                        password=PASSWORD,                             
                                        db=DB_NAME,
                                        charset='utf8mb4',
                                        cursorclass=pymysql.cursors.DictCursor) 

    def get_connection(self):
        return self.connection

    def close_connection(self):
        return self.connection.close()