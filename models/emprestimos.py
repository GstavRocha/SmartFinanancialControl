import sys
from pathlib import Path
from datetime import datetime

# Adiciona o diretório raiz ao sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from Database_Manager import Database_Manager
from models.query_util import Query_Util
from models.DAO_utils import BaseDAO
from models.validators.date_validation import mounths

class EmprestimosDAO(BaseDAO):
    def __init__(self):
        db = Database_Manager()
        query = Query_Util(db)
        self.valor = "valor_principal"
        self.juros = "juros_mensal"
        self.data = "data_emprestimo"
        self.emprestimo = "data_emprestimo"
        self.parcelas = "numero_parcelas"
        self.pagamento = "data_pagamento"
        self.status = "status"

        super().__init__(
            table_name="emprestimos",
            primary_key="id_emprestimos",
            query_util=query
        )
    
    def get_all_emprestimos(self):
        return self.get_all()
    
    def get_emprestimo_by_id(self, id):
        return self.get_by_id(id)
    
    def get_valor_by_id(self,id):
        return self.find_a(self.valor,self.primary_key,id)
    """
    Como resolver vencimento?
    """
    def get_vencimento_by_id(self, id):
        return self.find_a(self.emprestimo, self.primary_key, id)
    
    def get_juros_by_id(self, id):
        return self.find_a(self.juros, self.primary_key, id)
    
    def get_numero_parcelas_by_id(self, id):
        return self.find_a(self.parcelas, self.primary_key, id)
    
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
    
    def update_valor_by_id(self, value, id):
        new_value = { self.valor: value}
        old_value = self.get_valor_by_id(id)
        if new_value == old_value:
            return {"json": 400}
        else:
            return self.update(id, new_value)
    
    def add_value_to_valor_by_id(self, value, id):
        value_data = self.get_valor_by_id(id)
        new_valor = float(value)
        real_value = value_data[self.valor] + new_valor
        update_value = {self.valor: real_value}
        return self.update(id, update_value)
    def update_date_by_id(self, day, mounth):
        today = day
        mounthly = mounths[mounth]
        year = datetime.now()
        full_date = {self.data: f"{day}/{mounthly}/{year.year}"}
        return full_date
        
    
    def delete_value_to_by_id(self, id):
        old_value = self.get_valor_by_id(id)
        update_value = old_value[self.valor]
        if update_value > 0.1:
            self.update(id,{self.valor: 0})
            return self.get_valor_by_id(2)
        self.update(id,{self.valor: 0})
        return self.get_valor_by_id(id)
    def close(self):
        self.db.close()