from models.clientes import ClientesDAO


class Clientes_service:
    def __init__(self):
        self.dao = ClientesDAO()

    def create_cliente(self, nome:str, contato: str, email: str, endereco: str, foto:str):
        return self.dao.insert_cliente(
            nome=nome,
            contato=contato,
            email=email,
            endereco=endereco,
            foto=foto,
        )
    
    def get_all_clientes(self):
        return self.dao.get_all()
    
    def get_cliente_by_id(self, id: int):
        return self.dao.get_cliente_by_id(id=id)
    
    def get_nome_cliente(self, id: int):
        return self.dao.get_nome_by_id(id=id)
    
    def get_contato_cliente(self, id: int):
        return self.dao.get_contato_by_id(id=id) 
    
    def get_endereco_cliente(self, id: int):
        return self.dao.get_endereco_by_id(id=id)
    
    def get_email_cliente(self, id: int):
        return self.dao.get_email_by_id(id=id)
    
    def get_photo_cliente(self, id: int):
        return self.dao.get_photo_by_id(id=id)
    
    def get_cliente_atualizado_data(self, id: int):
        return self.dao.get_atualizado_by_id(id=id)
    
    def update_cliente(self, id: int, nome: str, contato: str, endereco: str, email: str, foto: str):
        return self.dao.update_cliente_by_id(id=id)
    
    def update_nome_cliente(self, id: int, nome: str):
        return self.dao.update_nome_by_id(id=id, nome=nome)
    
    def update_contato_cliente(self, id: int, contato: str):
        return self.dao.update_contato_by_id(id=id, contato=contato)
    
    def update_email_cliente(self, id: int, email:str):
        return self.dao.update_email_by_id(id=id,email=email)
    
    def update_endereco_cliente(self, id: int, endereco: str):
        return self.dao.update_endereco_by_id(id=id, endereco=endereco)
    
    def update_photo_cliente(self, id: int, photo: str):
        return self.dao.update_photo_by_id(id=id,photo=photo)
    
    def delete_cliente(self, id):
        return self.dao.delete_cliente_by_id(id=id)
        