from models.pagamentos import PagamentosDAO


class Pagamentos_service:
    def __init__(self):
        self.dao = PagamentosDAO()

    def create_pagamento(
        self, id_parcelas: int, valor: float, day: int, mounth: str, observacao: str
    ):
        return self.dao.insert_pagamentos(
            id_parcelas=id_parcelas,
            valor=valor,
            day=day,
            mounth=mounth,
            observacao=observacao,
        )

    def get_all_pagamentos(self):
        return self.dao.get_all_pagamentos()

    def get_pagamento_by_id(self, id: int):
        return self.dao.get_pagamentos_by_id(id=id)

    def get_id_parcelas_pagamento(self, id: int):
        return self.dao.get_id_parcelas_by_id(id=id)

    def get_valor_pago_pagamento(self, id: int):
        return self.dao.get_valor_pago_by_id(id=id)

    def get_data_pagamento(self, id: int):
        return self.dao.get_data_by_id(id=id)

    def get_observacao_pagamento(self, id: int):
        return self.dao.get_observacao_by_id(id=id)

    # def update_pagamento(
    #     self,
    #     id: int,
    #     id_parcelas: int,
    #     valor: float,
    #     day: int,
    #     mounth: str,
    #     observacao: str,
    # ):
    #     return self.dao.update_pagamento_by_id(id=id)

    def update_id_parcelas_pagamento(self, id: int, id_parcelas: int):
        return self.dao.update_id_parcelas_by_id(id=id, param_id=id_parcelas)

    def update_valor_pago_pagamento(self, id: int, valor: float):
        return self.dao.update_valor_pago_by_id(id=id, valor=valor)

    def update_data_pagamento(self, id: int, day: int, mounth: str):
        return self.dao.update_data_by_id(id=id, day=day, mounth=mounth)

    def update_observacao_pagamento(self, id: int, observacao: str):
        return self.dao.update_observacao(id=id, observacao=observacao)

    def delete_pagamento(self, id: int):
        return self.dao.delete_parcelas(id=id)
