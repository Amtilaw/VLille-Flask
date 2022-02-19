import pymysql.cursors 
import os
from dotenv import dotenv_values
from pathlib import Path
config = dotenv_values(".env")

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