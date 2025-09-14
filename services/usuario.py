from models.usuarios import UsuarioDAO
from typing import Optional, List, Dict, Any, Tuple
from services.validators.validacao import (
    is_validate_email,
    validade_required_fields,
    ValidationError,
)


class Usuario_service:
    def __init__(self):
        self.dao = UsuarioDAO()

    def criar_usuario(self, nome: str, email: str, password: str):
        payload = {"nome": nome, "email": email, "password": password}
        validade_required_fields(payload, ["nome", "email", "password"])
        if not is_validate_email(email):
            raise ValidationError("E-mail inválido")
        return self.dao.insert_usuario(nome=nome, email=email, password=password)