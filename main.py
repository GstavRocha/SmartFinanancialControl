import tkinter as tk
from pathlib import Path
import sys
from pathlib import Path
from Database_Manager import Database_Manager
from models.query_util import Query_Util
import time

# Adiciona o diretório raiz ao sys.path, garantindo acesso à Database_Manager.py
sys.path.append(str(Path(__file__).resolve().parent.parent))

from services.validators.validacao import is_validate_email, validade_required_fields
from services.validators.execptionsp import (
    ValidationError,
    NotFoundError,
    ConflictError,
)
from services.usuario import Usuario_service
from services.clientes import Clientes_service
from services.pagamentos import Pagamentos_service
from services.parcelas import Parcelas_service
# from models.clientes import ClientesDAO
# from models.emprestimos import EmprestimosDAO
# from models.parcelas import ParcelasDAO
# from models.pagamentos import PagamentosDAO
from models.usuarios import UsuarioDAO

version = tk.TkVersion


def main():
    # Query_Util(Database_Manager())
    # clientes = ClientesDAO()
    # emprestimos = EmprestimosDAO()
    # parcelas = ParcelasDAO()
    # paga = PagamentosDAO()
    user = UsuarioDAO()
    user_service = Usuario_service()
    cliente_service = Clientes_service()
    pagamentos = Pagamentos_service()
    parcelas = Parcelas_service()
    
    check = pagamentos.get_data_pagamento(2)
    teste = parcelas.get_numero_emprestimo(1)
    # ver = user.get_all_usuarios()
    print(teste)


if __name__ == "__main__":
    main()
