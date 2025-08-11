import tkinter as tk
from pathlib import Path
import sys
from pathlib import Path
from Database_Manager import Database_Manager
from models.query_util import Query_Util

# Adiciona o diretório raiz ao sys.path, garantindo acesso à Database_Manager.py
sys.path.append(str(Path(__file__).resolve().parent.parent))

from models.clientes import ClientesDAO
version = tk.TkVersion


if __name__ == '__main__':
    Query_Util(Database_Manager())
    clientes = ClientesDAO()
    # novo = clientes.create({
    #     "nome_cliente": "Debora",
    #     "contato_cliente": "2323232323",
    #     "email_cliente": "beba@gmail.com",
    #     "endereco_cliente": "rua da Cocada",
    #     "foto_cliente": "Teste/.//"
    # })
    teste = clientes.select_first_photo(26)
    todos = clientes.get_all()
    gustavo = {
        "nome_cliente": "Debora2",
        "contato_cliente": "2323232323",
        "email_cliente": "beba@gmail.com",
        "endereco_cliente": "rua da Cocada",
        "foto_cliente": "Teste/.//"
    }
    upate = clientes.delete(26)
    
    print(todos)
    # get_cliente = clientes.get_cliente_by_id(26)
    # print(get_cliente)
    


