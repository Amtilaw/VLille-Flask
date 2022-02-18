import pymysql.cursors 

class Bdd:
   
    def __init__(self): 
        self.connection = pymysql.connect(host='localhost',
                                        user='root',
                                        password='',                             
                                        db='pythonVlille',
                                        charset='utf8mb4',
                                        cursorclass=pymysql.cursors.DictCursor) 

    def get_connection(self):
        return self.connection

    def close_connection(self):
        return self.connection.close()