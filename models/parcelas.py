import sys
from pathlib import Path
from datetime import datetime

# Adiciona o diretório raiz ao sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from Database_Manager import Database_Manager
from models.query_util import Query_Util
from models.DAO_utils import BaseDAO

status = {
    1: "pendente",
    2: "pago",
    3: "atrasado"
}
# Fazer rotina de verificação, parcelas pagamento não pode ser menor que data,
# não pode uma pessoa pagar antes de ter gerado a divida.
class ParcelasDAO(BaseDAO):
    def __init__(self):
        db = Database_Manager()
        query = Query_Util(db)
        self.id_parcelas = "id_parcelas"
        self.numero_emprestimo = "numero_emprestimo"
        self.valor = "valor_parcela"
        self.vencimento = "data_vencimento"
        self.pagamento  = "data_pagamento"
        self.status = "status"
        self.id_emprestimo = "id_emprestimo"
        super().__init__(
            table_name="parcelas",
            primary_key=self.id_parcelas,
            query_util=query
        )
    def get_all_parcelas(self):
        return self.get_all()
    
    def get_parcelas_by_id(self,id):
        return self.get_by_id(id)
    
    def get_numero_emprestimos_by_id(self, id):
        return self.find_a(self.numero_emprestimo,self.id_parcelas, id)
    
    def get_valor_parcelas_by_id(self, id):
        return self.find_a(self.valor, self.id_parcelas,id)
    
    def get_vencimento_by_id(self, id):
        return self.find_a(self.vencimento, self.id_parcelas, id)
    
    def get_pagamento_by_id(self, id):
        return self.find_a(self.pagamento, self.id_parcelas, id)
    
    # pega o primeiro
    def get_status_by_id(self, id):
        return self.get_by_id(id)
    
    def get_all_parcelas_by_id_emprestimo(self, id):
        return self.find_a(self.valor, self.id_emprestimo, id)
    
    def get_all_data_parcelas_by_id(self, id):
        return self.find_a(self.vencimento,self.id_emprestimo, id)
    
    def get_all_pagamentos_by_id(self, id):
        return self.find_a(self.pagamento, self.id_emprestimo, id)
    
    def insert_parcelas(self, numero_emprestimo, valor, data_vencimento, data_pagamento, num_status, id_emprestimo):
        new_parcelas = {
            self.numero_emprestimo: numero_emprestimo,
            self.valor: valor,
            self.vencimento: data_vencimento,
            self.pagamento: data_pagamento,
            self.status: status[num_status],
            self.id_emprestimo: id_emprestimo
        }
        return self.create(new_parcelas)
    
    def update_parcelas_by_id(self, id, numero_emprestimo, valor, data, pagamento, num_status,id_emprestimo):
        new_parcelas = {
            self.numero_emprestimo: numero_emprestimo,
            self.valor: valor,
            self.vencimento: data,
            self.pagamento: pagamento,
            self.status: status[num_status],
            self.id_emprestimo: id_emprestimo
        }
        update = self.update(id, new_parcelas)
        if update == 0:
            return {"json":400}
        else:
            return self.update(id, new_parcelas)
    
    # O que isso faz? Adiciona uma nova parcela? 
    def add_numero_emprestimo(self, id):
        old_numero = self.get_numero_emprestimos_by_id(id)
        first_number = old_numero[self.numero_emprestimo]
    
        return first_number
    
    def delete_parcela(self, id):
        return self.delete(id)