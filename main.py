import tkinter as tk
from pathlib import Path
import sys
from pathlib import Path
from Database_Manager import Database_Manager
from models.query_util import Query_Util
import time

# Adiciona o diretório raiz ao sys.path, garantindo acesso à Database_Manager.py
sys.path.append(str(Path(__file__).resolve().parent.parent))

from models.clientes import ClientesDAO
from models.emprestimos import EmprestimosDAO
version = tk.TkVersion


if __name__ == '__main__':
    Query_Util(Database_Manager())
    clientes = ClientesDAO()
    emprestimos = EmprestimosDAO()
    # all_clientes = clientes.get_all()

    check  = emprestimos.add_value_to_valor_by_id(5.2,2)
    print(check)
    time.sleep(2.0)
    verify = emprestimos.get_valor_by_id(2)
    print(verify)

    # emprestimo = emprestimos.insert_emprestimos(2, 100,2,"dasda",12,"ativo")
    # print(insert)

