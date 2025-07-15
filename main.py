import tkinter as tk
from pathlib import Path
import sys
from pathlib import Path

# Adiciona o diretório raiz ao sys.path, garantindo acesso à Database_Manager.py
sys.path.append(str(Path(__file__).resolve().parent.parent))

from models.clientes import 
version = tk.TkVersion


if __name__ == '__main__':
    print(version)

