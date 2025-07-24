import tkinter as tk
from pathlib import Path
import sys
from pathlib import Path
from Database_Manager import Database_Manager

# Adiciona o diretório raiz ao sys.path, garantindo acesso à Database_Manager.py
sys.path.append(str(Path(__file__).resolve().parent.parent))

from models.clientes import ClientesDAO
version = tk.TkVersion


if __name__ == '__main__':
    clientes = ClientesDAO()
    # check = clientes.insert_clientes("Gustavo2", "99999999","nooseguitar@hotmail.com","ruta teste",".///l", )
    getAllclientes = clientes.get_id_cliente(1)
    print(getAllclientes)

    


