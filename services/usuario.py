from models.usuarios import UsuarioDAO
from typing import Optional, List, Dict, Any, Tuple

class Usuario_service:
    def __init__(self):
        self.dao = UsuarioDAO()

    def create_user(self, nome: str, email: str, password: str):
        return self.dao.insert_usuario(nome=nome, email=email, password=password)

    def get_all_users(self):
        return self.dao.get_all()

    def get_user_by_id(self, id: int):
        return self.dao.get_usuarios_by_id(id)

    def update_user(self, id: int, nome: str, email: str, password: str):
        return self.dao.update_usuario(id=id, nome=nome, email=email, password=password)

    def update_password(self, id: int, password: str):
        return self.dao.update_password_by_id(id=id, password=password)

    def update_name(self, id: int, nome: str):
        return self.dao.update_nome_by_id(id=id, nome=nome)

    def update_email(self, id: int, email: str):
        return self.dao.update_email_by_id(id=id, email=email)

    def delete(self, id):
        return self.dao.delete_usuario_by_id(id=id)
