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

    def insert(self, id_cliente: int, valor: float, juros: float, date: str, numero: int, status: )