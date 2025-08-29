
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
        self.nome = "nome_cliente"
        self.contato = "contato_cliente"
        self.email = "email_cliente"
        self.endereco = "endereco_cliente"
        self.foto = "foto_cliente"
        self.atualizado = "atualizado_em"
        super().__init__(
            table_name="clientes",
            primary_key="id_cliente",
            query_util=query
        )

    def get_all_clientes(self):
        return self.get_all()
    
    def get_cliente_by_id(self, id):
        return self.get_by_id(id)
    
    def get_nome_by_id(self, id):
        return self.find_a(self.nome, self.primary_key, id)
    
    def get_contato_by_id(self, id):
        return self.find_a(self.contato, self.primary_key, id)
    
    def get_endereco_by_id(self, id):
        return self.find_a(self.endereco, self.primary_key, id)
    
    def get_email_by_id(self, id):
        return self.find_a(self.email,self.primary_key, id)
            
    def get_photo_by_id(self,id):
        return self.find_a(self.foto,self.primary_key,id)
    
    def get_atualizado_by_id(self, id):
        return self.find_a(self.atualizado, self.primary_key , id)
    
    def insert_cliente(self, nome, contato, email, endereco, foto):
        novo_cliente = {
            self.nome: nome,
            self.contato: contato,
            self.endereco: endereco,
            self.email: email,
            self.foto: foto
        }
        return  self.create(novo_cliente)
    
    def update_nome_by_id(self, id, nome):
        return self.update(id,{self.nome: nome})
    
    def update_contato_by_id(self, id, contato):
        return self.update(id, {self.contato: contato})
    
    def update_email_by_id(self,id, email):
        return self.update(id, {self.email: email})
    
    def update_endereco_by_id(self, id, endereco):
        return self.update(id,{self.endereco: endereco})
    
    def update_photo_by_id(self, id, photo):
        return self.update(id, {self.foto: photo})
    
    def update_cliente_by_id(self,id ,nome, contato, endereco, email, foto ):
        update_cliente = {
            self.nome : nome,
            self.contato : contato,
            self.endereco : endereco,
            self.email : email,
            self.foto: foto
        }
        return self.update(id,update_cliente)
    
    def delete_cliente_by_id(self, id):
        if self.delete(id) == 1:
            return "user has deleted"
        else:
            return "user hasn't deleted"
        
    def close(self):
        self.db.close()
        