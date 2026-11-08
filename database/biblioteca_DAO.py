from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_all_biblioteche(self):
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Errore di connessione al database")
            return []
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM biblioteca"""
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(Biblioteca(**row))
        cursor.close()
        cnx.close()
        return result

