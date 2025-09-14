import re
from models.clientes import ClientesDAO
from models.usuarios import UsuarioDAO
from .execptionsp import ValidationError, NotFoundError, ConflictError
from typing import Optional, List, Dict, Any, Tuple, Sequence, Mapping

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def is_validate_email(email: str | None) -> bool:
    if not email:  # decide se vazio conta como válido
        return False
    return EMAIL_RE.fullmatch(email) is not None


def validade_required_fields(data: UsuarioDAO) -> None:
    if not data.nome or not data.email or not data.password:
        raise ValidationError("Campos obrigatórios: nome, email, passwrord")


def validade_required_fields(data: Mapping[str, Any], required: Sequence[str]) -> None:
    faltando = [k for k in required if not data.get(k)]
    if faltando:
        raise ValidationError(f"Campos obrigatórios faltando: {', '.join(faltando)}")
