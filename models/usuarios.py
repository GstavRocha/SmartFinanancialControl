
import sys
from pathlib import Path

# Adiciona o diretório raiz ao sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from Database_Manager import Database_Manager
from models.query_util import Query_Util
from models.DAO_utils import BaseDAO

class UsuarioDAO(BaseDAO):
    def __init__(self):
        db = Database_Manager()
        query = Query_Util(db)
        self.id_usuarios="id_usuarios"
        self.nome = "nome"
        self.email="email"
        self.password= "password"
        super().__init__(
            table_name="usuarios",
            primary_key="id_usuarios",
            query_util=query
        )
    def get_all_usuarios(self):
        return self.get_all()
    
    def get_usuarios_by_id(self,id):
        return self.get_by_id(id)
    
    def get_nome_by_id(self, id):
        return self.find_a(self.nome, self.primary_key,id)
    def 
    def insert_usuario(self, nome, email, password):
        new_usuario = {
            self.nome: nome,
            self.email: email,
            self.password: password
        }
        return self.create(new_usuario)

        # CREATE TABLE IF NOT EXISTS usuarios (
        #     id_usuarios INTEGER PRIMARY KEY AUTOINCREMENT,
        #     nome TEXT NOT NULL,
        #     email TEXT NOT NULL UNIQUE,
        #     password TEXT NOT NULL
        # );