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
from models.parcelas import ParcelasDAO

version = tk.TkVersion


if __name__ == '__main__':
    Query_Util(Database_Manager())
    clientes = ClientesDAO()
    emprestimos = EmprestimosDAO()
    parcelas = ParcelasDAO()
    # all_clientes = clientes.get_all()
    # todas = parcelas.get_status_by_id(1)
    # todas = parcelas.get_all()
    # insert  = parcelas.add_numero_emprestimo(1,3)
    emprestimos.add_value_to_valor_by_id(1, 2.0)
    
    # time.sleep(1.0)
    # print(pr)
    # print("-----\n")
    # emprestimo = emprestimos.insert_emprestimos(2, 100,2,"dasda",12,"ativo")
    # print(insert)

