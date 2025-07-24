import tkinter as tk
from pathlib import Path
import sys
from pathlib import Path

# Adiciona o diretório raiz ao sys.path, garantindo acesso à Database_Manager.py
sys.path.append(str(Path(__file__).resolve().parent.parent))

from models.clientes import ClientesDAO
version = tk.TkVersion


if __name__ == '__main__':
    clientes = ClientesDAO()
    clientes.insert_clientes("Gustavo", "99999999","nooseguitar@hotmail.com","ruta teste",".///l")
    print(clientes.get_all_clientes())
    
    print(version)

