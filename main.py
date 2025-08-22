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
    verify = parcelas.get_all_parcelas_by_id_emprestimo(1)
    todas = parcelas.get_all()
    # insert  = parcelas.insert_parcelas(6,300,"10/10/2025","08/10/2025",2,1)

    
    # time.sleep(1.0)
    print(verify)
    print("-----\n")
    print(todas)

    # emprestimo = emprestimos.insert_emprestimos(2, 100,2,"dasda",12,"ativo")
    # print(insert)

