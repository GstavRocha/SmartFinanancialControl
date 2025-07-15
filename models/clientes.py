
import sys
from pathlib import Path

# Adiciona o diretório raiz ao sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from Database_Manager import Database_Manager

class ClientesDAO:
    def __init__(self):
        self.db = Database_Manager()
        
    def insert_clientes(self, nome, contato, email, endereco, foto=None):
        self.db.cursor.execute("""
                               INSERT INTO clientes (nome_cliente, contato_cliente, email__cliente, endereco, foto_cliente)
                               VALUES(?,?,?,?,?,?)
                               """,(nome, contato, email, endereco, foto))
        self.db.conn.commit()
        
    def get_all_clientes(self):
        self.db.cursor.execute("""
                               SELECT * FROM clientes;
                               """)
        self.db.conn.commit()
    def close(self):
        self.db.close()
        
teste = ClientesDAO()
novo = teste.insert_clientes("Gustavo","9999999","gmail@email",None)