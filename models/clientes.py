
import sys
from pathlib import Path

# Adiciona o diretório raiz ao sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from Database_Manager import Database_Manager

class ClientesDAO:
    def __init__(self):
        self.db = Database_Manager()
        self.db.inicializar_tabelas()
        
    def insert_clientes(self, nome, contato, email, endereco, foto=None):
        self.db.reconnect()
        self.db.cursor.execute("""
        INSERT INTO clientes (nome_cliente, contato_cliente, email_cliente, endereco_cliente, foto_cliente)
        VALUES(?,?,?,?,?)
        """,(nome, contato, email, endereco, foto))
        clientes = self.db.cursor.fetchall()
        self.db.conn.commit()
        self.db.conn.close()
        return clientes
        
    def get_all_clientes(self):
        self.db.reconnect()
        self.db.cursor.execute("SELECT * FROM clientes;")
        result = self.db.cursor.fetchall()
        self.db.conn.commit()
        self.db.conn.close()
        return result
    def get_id_cliente(self, id):
        self.db._connect()
        self.db.cursor.execute(f"SELECT * FROM clientes WHERE id_cliente = {id};")
        result  = self.db.cursor.fetchone()
        self.db.conn.commit()
        self.db.conn.close()        
        return result
    def search_cliente(self, )
    def close(self):
        self.db.close()
        