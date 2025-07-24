
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
        try:
            self.db.reconnect()
            self.db.cursor.execute("""
                           INSERT INTO clientes (nome_cliente, contato_cliente, email_cliente, endereco_cliente, foto_cliente)
                           VALUES(?,?,?,?,?)
                           """,(nome, contato, email, endereco, foto))
        finally:
            self.db.close()
        
    def get_all_clientes(self):
        self.db.cursor.execute("""
                               SELECT * FROM clientes;
                               """)
        self.db.conn.commit()
        self.db.conn.close()
    def close(self):
        self.db.close()
        