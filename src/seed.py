from pathlib import Path
import sys

# Garante que o Python ache o módulo correto (ajusta sys.path)
sys.path.append(str(Path(__file__).resolve().parent))

from db import Database_Manager  # importe correto do arquivo onde está a classe

if __name__ == "__main__":
    db = Database_Manager()             # instância da classe
    db.inicializar_tabelas()            # cria todas as tabelas
    print("✅ Tabelas criadas com sucesso!")
    db.close()