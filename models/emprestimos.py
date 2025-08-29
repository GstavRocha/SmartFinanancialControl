import sys
from pathlib import Path
from datetime import datetime

# Adiciona o diretório raiz ao sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from Database_Manager import Database_Manager
from models.query_util import Query_Util
from models.DAO_utils import BaseDAO
from models.validators.date_validation import mounths
from models.validators.status_validation import status_emprestimo


class EmprestimosDAO(BaseDAO):
    def __init__(self):
        db = Database_Manager()
        query = Query_Util(db)
        self.cliente = "id_cliente"
        self.valor = "valor_principal"
        self.juros = "juros_mensal"
        self.data = "data_emprestimo"
        self.parcelas = "numero_parcelas"
        self.status = "status"

        super().__init__(
            table_name="emprestimos",
            primary_key="id_emprestimos",
            query_util=query
        )
    
    def get_all_emprestimos(self):
        return self.get_all()
    
    def get_emprestimo_by_id(self, id):
        return self.find_a(self.data, self.primary_key, id)
    """
    indexar id com nome, tem que trazer nome não id
    """
    def get_cliente_by_id(self, id):
        return self.find_a(self.cliente, self.primary_key, id)
    
    def get_valor_by_id(self,id):
        return self.find_a(self.valor,self.primary_key,id)
    """
    Como resolver vencimento?
    """
    def get_juros_by_id(self, id):
        return self.find_a(self.juros, self.primary_key, id)

    def get_data_by_id(self, id):
        return self.find_a(self.data, self.primary_key, id)
    
    def get_juros_by_id(self, id):
        """
        FAZER O CALCULO DE JUROS SOBRE JUROS EM REFRÊNCIA AOS DIAS
        """
        return self.find_a(self.juros, self.primary_key, id)
    
    def get_numero_parcelas_by_id(self, id):
        return self.find_a(self.parcelas, self.primary_key, id)
    
    def get_status_by_id(self, id):
        return self.find_a(self.status, self.primary_key, id)
    
    def insert_emprestimos(self,id_cliente, valor, juros_mensal, data, numero_parcelas, status):
        new_emprestimo = {
            self.cliente: id_cliente,
            self.valor: valor,
            self.juros: juros_mensal,
            self.data: data,
            self.parcelas: numero_parcelas,
            self.status: status
        }
        return self.create(new_emprestimo)
    
    def update_valor_by_id(self, value, id):
        new_value = { self.valor: value}
        old_value = self.get_valor_by_id(id)
        if new_value == old_value:
            return {"json": 400}
        else:
            return self.update(id, new_value)
        
    def update_juros_by_id(self, id, juros):
        float_juros = float(juros)
        new_juros = {self.juros: float_juros}
        return self.update(id, new_juros)
    
    def add_value_to_valor_by_id(self, id, value):
        value_data = self.get_valor_by_id(id)
        new_valor = float(value)
        real_value = value_data[0]
        add_value = real_value[self.valor] + new_valor
        return {self.valor: add_value}
    
    def update_data_by_id(self, id, day, mounth):
        """
        day deve passar "01" para ter o zero na frente da dia
        """
        mounthly = mounths[mounth]
        year = datetime.now()
        full_date = {self.data: f"{day}/{mounthly}/{year.year}"}
        return self.update(id, full_date)    
    
    def update_parcelas_by_id(self, id, parcelas):
        int_parcelas = int(parcelas)
        new_parcelas = {self.parcelas: int_parcelas}
        return self.update(id, new_parcelas)
    
    def update_status_by_id(self, id, num):
        return self.update(id, {self.status: status_emprestimo[num]})
    
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