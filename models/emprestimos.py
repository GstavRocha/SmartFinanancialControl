import sys
from pathlib import Path

# Adiciona o diretório raiz ao sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from Database_Manager import Database_Manager
from models.query_util import Query_Util
from models.DAO_utils import BaseDAO

class EmprestimosDAO(BaseDAO):
    def __init__(self):
        db = Database_Manager()
        query = Query_Util(db)
        super().__init__(
            table_name="emprestimos",
            primary_key="id_emprestimos",
            query_util=query
        )
    def get_all_emprestimos(self):
        return self.get_all()
    def get_emprestimo_by_id(self, id):
        return self.get_by_id(id)
    
    def insert_emprestimos(self,id_cliente, valor, juros_mensal, data, numero_parcelas, status):
        new_emprestimo = {
            "id_cliente": id_cliente,
            "valor_principal": valor,
            "juros_mensal": juros_mensal,
            "data_emprestimo": data,
            "numero_parcelas": numero_parcelas,
            "status": status
        }
        return self.create(new_emprestimo)
        
    def close(self):
        self.db.close()