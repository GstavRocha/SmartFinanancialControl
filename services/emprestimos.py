from models.emprestimos import EmprestimosDAO


class Emprestimos_service:
    def __init__(self):
        self.dao = EmprestimosDAO()

    def get_all(self):
        return self.dao.get_all()

    def get_id(self, id: int):
        return self.dao.get_by_id(id)

    def get_client(self, id: int):
        return self.dao.get_cliente_by_id(id=id)

    def get_valor(self, id: int):
        return self.dao.get_valor_by_id(id)

    # aqui vem a base de calculos
    def get_juros(self):
        return self.dao.get_juros_by_id(id=id)

    def get_numero_parcelas(self, id: int):
        return self.dao.get_numero_parcelas_by_id(id=id)

    def get_status(self, id: int):
        return self.dao.get_status_by_id(id=id)

    def insert(
        self,
        id_cliente: int,
        valor: float,
        juros: float,
        date: str,
        numero: int,
        status: int,
    ):
        return self.dao.insert_emprestimos(
            id_cliente=id_cliente,
            valor=valor,
            juros_mensal=juros,
            data=date,
            numero_parcelas=numero,
            num_status=status,
        )
    
    def update_valor(self, value: float, id: int):
        return self.dao.update_valor_by_id(value=value, id=id)
    
    def update_juros_by(self, id: int, juros: float):
        return self.dao.update_juros_by_id(id=id, juros=juros)
    
    def update_date(self, id: int, day: int, mounth: int):
        return self.dao.update_data_by_id(id=id, day=day, mounth=mounth)
    
    def update_parcelas(self, id: int, parcelas: int):
        return self.dao.update_parcelas_by_id(id=id, parcelas=parcelas)
    
    def update_status(self, id: int, status_num: int):
        return self.dao.update_status_by_id(id=id, num=status_num)
    
    def add_valor(self, id: int, value: float):
        return self.dao.add_value_to_valor_by_id(id=id, value=value)
    
    def delete_emprestimo(self, id: int):
        return self.dao.delete_value_to_by_id(id=id)
    