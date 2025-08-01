from Database_Manager import Database_Manager

class Query_Util:
    def __init__(self, database):
        self.db = database
        self.db.inicializar_tabelas()
        
    def select_all(self, table):
        conn = self.db._connect()
        print(conn)