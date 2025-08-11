
import sys
from pathlib import Path

# Adiciona o diretório raiz ao sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from Database_Manager import Database_Manager
from models.query_util import Query_Util
from models.DAO_utils import BaseDAO


class ClientesDAO(BaseDAO):
    def __init__(self):
        db = Database_Manager()
        query = Query_Util(db)
        super().__init__(
            table_name="clientes",
            primary_key="id_cliente",
            query_util=query
        )

    def get_all_clientes(self):
        return self.get_all("clientes")
    
    def get_cliente_by_id(self, cliente_id):
        return self.get_by_id(cliente_id)

    def insert_cliente(self, nome, contato, email, endereco, foto):
        novo_cliente = {
            "nome_cliente": nome,
            "contato_cliente": contato,
            "endereco_cliente": endereco,
            "email_cliente": email,
            "foto_cliente": foto
        }
        return self.create(novo_cliente)
    
    def find_cliente_by_id(self, id):
        return self.find_a("foto_cliente",self.primary_key, id)
    
    def select_first_photo(self,id):
        return self.find_a("foto_cliente",self.primary_key,id)
    
    def update_cliente_by_id(self,id ,nome, contato, endereco, email, foto ):
        update_cliente = {
            "nome_cliente": nome,
            "contato_cliente": contato,
            "endereco_cliente": endereco,
            "email_cliente": email,
            "foto_cliente": foto
        }
        return self.update(id,update_cliente)
    def delete_cliente_by_id(self, id):
        if self.delete(id) == 1:
            return "user has deleted"
        else:
            return "user hasn't deleted"
    def close(self):
        self.db.close()
        