from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_all_libri(self, nome_biblioteca=None, genere=None):
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Errore di connessione al database")
            return []
        cursor = cnx.cursor(dictionary=True)
        query = """
            SELECT l.id, l.titolo, l.autore, l.genere, l.anno_pubblicazione, l.id_biblioteca
            FROM libro l
            JOIN biblioteca b ON l.id_biblioteca = b.id
            WHERE b.nome = COALESCE(%s, b.nome)
              AND l.genere = COALESCE(%s, l.genere)
            ORDER BY l.titolo ASC
        """
        cursor.execute(query, (nome_biblioteca,genere))
        libri = []
        for row in cursor:
            libri.append(Libro(**row))
        cursor.close()
        cnx.close()
        return libri

    def get_all_generi(self):
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Errore di connessione al database")
            return []
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT DISTINCT genere FROM libro"""
        cursor.execute(query)
        generi = []
        for row in cursor:
            generi.append(row["genere"])
        cursor.close()
        cnx.close()
        return generi