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

class PagamentosDAO(BaseDAO):
    def __init__(self):
        db = Database_Manager()
        query = Query_Util(db)
        self.id_parcelas = "id_parcelas"
        self.valor_pago = "valor_pago"
        self.data = "data_pagamento"
        self.observacao = "observacao"
        super().__init__(
            table_name="pagamentos",
            primary_key="id_pagamentos",
            query_util=query
        )
    
    def get_all_pagamentos(self):
        return self.get_all()
    
    def get_pagamentos_by_id(self, id):
        return self.get_by_id(id)
    
    def get_id_parcelas_by_id(self, id):
        return self.find_a(self.id_parcelas, self.primary_key, id)
    
    def get_valor_pago_by_id(self, id):
        return self.find_a(self.valor_pago, self.primary_key, id)
    
    def get_data_by_id(self, id):
        return self.find_a(self.data, self.primary_key, id)
    
    def get_observacao_by_id(self, id):
        return self.find_a(self.observacao, self.primary_key, id)
    
    def insert_pagamentos(self, id_parcelas,valor,day, mounth, observacao):
        mountly = mounths[mounth]
        year = datetime.now()
        new_pagamento = {
            self.id_parcelas: id_parcelas,
            self.valor_pago: valor,
            self.data: f"{day}/{mountly}/{year}",
            self.observacao: observacao,
        }
        return self.create(new_pagamento)
    
    def update_id_parcelas_by_id(self, id, param_id):
        old_id = self.get_id_parcelas_by_id(id)
        new_id = self.get_id_parcelas_by_id(id)
        real_id = old_id[0]
        real_new_id = new_id[0]
        check_value = real_id[self.id_parcelas]
        check_new_value = real_new_id[self.id_parcelas]

        if check_value is not None and check_new_value is not None:
            return self.update(id,{self.id_parcelas: param_id})
        else:
            print(" Vazio")
    
    def update_valor_pago_by_id(self, id, valor):
        check_id = self.get_valor_pago_by_id(id)
        real_id = check_id[0]
        check_value = real_id[self.valor_pago]
        if check_value is not None:
            return self.update(id, {self.valor_pago: valor})
        else:
            print("Empty value")
    
    def update_data_by_id(self,id, day, mounth):
        check_day = int(day) # ajustar para string
        mounthly = mounths[mounth]
        year = datetime.now()
        check_data = self.get_data_by_id(id)
        full_data = {self.data: f"{check_day}/{mounthly}/{year.year}"}
        if check_data is not None:
            return self.update(id, full_data)
        else:
            print("Empty id")
    def update_observacao(self, id, observacao):
        check_observacao = self.get_observacao_by_id(id)
        real_observacao = check_observacao[0]
        check_value = real_observacao[self.observacao]
        if check_value is not None:
            return self.update(id, {self.observacao: observacao})
        else:
            return {"Empty":400}

    def delete_parcelas(self, id):
        return self.delete(id)
    