from models.parcelas import ParcelasDAO


class Parcelas_service:
    def __init__(self):
        self.dao = ParcelasDAO()

    def create_parcelas(
        self,
        numero: int,
        valor: float,
        data_vencimento: str,
        data_pagamento: str,
        status: int,
        id_emprestimo: int,
    ):
        return self.dao.insert_parcelas(
            numero_emprestimo=numero,
            valor=valor,
            data_vencimento=data_vencimento,
            data_pagamento=data_pagamento,
            status=status,
            id_emprestimo=id_emprestimo,
        )
        
    
    def get_all_parcelas(self):
        return self.dao.get_all_parcelas()
    
    def get_parcela_by_id(self, id: int):
        return self.dao.get_all_pagamentos_by_id(id)

    def get_numero_emprestimo(self, id:int):
        return self.dao.get_numero_emprestimos_by_id(id)
    
    def get_valor_parcelas(self, id:int):
        return self.dao.get_valor_parcelas_by_id(id)
    
    def get_vencimento(self, id: int):
        return self.dao.get_vencimento_by_id(id=id)
    
    def get_pagamento(self, id: int):
        return self.dao.get_pagamento_by_id(id=id)
    
    def get_status(self, id: int):
        return self.dao.get_status_by_id(id=id)
    
    def get_parcelas_emprestismos(self, id: int):
        return self.dao.get_all_parcelas_by_id_emprestimo(id=id)
    
    def get_all_datas(self, id:int):
        return self.dao.get_all_data_parcelas_by_id(id=id)
    
    def get_all_pagamentos(self, id):
        return  self.dao.get_all_pagamentos_by_id(id=id)