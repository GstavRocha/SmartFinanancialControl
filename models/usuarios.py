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
        self.id_usuarios = "id_usuarios"
        self.nome = "nome"
        self.email = "email"
        self.password = "password"
        super().__init__(
            table_name="usuarios", primary_key="id_usuarios", query_util=query
        )

    def get_all_usuarios(self):
        return self.get_all()

    def get_usuarios_by_id(self, id):
        return self.get_by_id(id)

    def get_nome_by_id(self, id):
        return self.find_a(self.nome, self.primary_key, id)

    def get_email_by_id(self, id):
        return self.find_a(self.email, self.primary_key, id)

    def get_password_by_id(self, id):
        return self.find_a(self.password, self.primary_key, id)

    def insert_usuario(self, nome, email, password):
        new_usuario = {self.nome: nome, self.email: email, self.password: password}
        return self.create(new_usuario)

    def update_usuario(self, id, nome=None, email=None, password=None):
        """
        Atualiza parcialmente um usuário. Envie apenas os campos que deseja alterar.
        Ex.: update_usuario(5, nome="Novo Nome") ou update_usuario(5, email="a@b.com", password="123")
        Retorna o resultado do BaseDAO.update (ex.: linhas afetadas ou o registro atualizado, dependendo da implementação).
        """
        updates = {}
        if nome is not None:
            updates[self.nome] = nome
        if email is not None:
            updates[self.email] = email
        if password is not None:
            updates[self.password] = password

        if not updates:
            raise ValueError("Informe ao menos um campo para atualizar.")

        # Assumindo que o BaseDAO expõe update(id, data: dict)
        return self.update(id, updates)

    # Helpers de atualização (opcionais)
    def update_nome_by_id(self, id, nome):
        return self.update(id, {self.nome: nome})

    def update_email_by_id(self, id, email):
        return self.update(id, {self.email: email})

    def update_password_by_id(self, id, password):
        return self.update(id, {self.password: password})

    # ------- DELETE -------
    def delete_usuario_by_id(self, id):
        """
        Remove o usuário pelo ID (chave primária).
        Retorna o resultado do BaseDAO.delete (ex.: linhas afetadas).
        """
        return self.delete(id)
