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
            primary_key="id_parcelas",
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