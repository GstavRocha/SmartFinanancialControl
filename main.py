import customtkinter as ctk
from pathlib import Path
import sys
from pathlib import Path
from Database_Manager import Database_Manager
from models.query_util import Query_Util
import time

# Adiciona o diretório raiz ao sys.path, garantindo acesso à Database_Manager.py
sys.path.append(str(Path(__file__).resolve().parent.parent))

from services.validators.validacao import is_validate_email, validade_required_fields
from services.validators.execptionsp import (
    ValidationError,
    NotFoundError,
    ConflictError,
)
from services.usuario import Usuario_service
from services.clientes import Clientes_service
from services.pagamentos import Pagamentos_service
from services.parcelas import Parcelas_service
from services.emprestimos import Emprestimos_service

from views.login import Login_View

# version = tk.TkVersion

# def main():
#     # Query_Util(Database_Manager())
#     # clientes = ClientesDAO()
#     # emprestimos = EmprestimosDAO()
#     # parcelas = ParcelasDAO()
#     # paga = PagamentosDAO()
#     user = UsuarioDAO()
#     user_service = Usuario_service()
#     cliente_service = Clientes_service()
#     pagamentos = Pagamentos_service()
#     parcelas = Parcelas_service()
#     emprestimo = Emprestimos_service()
#     check = emprestimo.delete_emprestimo(1)

#     # ver = user.get_all_usuarios()
#     print(check)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title = "Controle de Investimentos"
        self.geometry = "480x520"
        self.minsize(420, 280)

        # Tela de Login
        self.login_view = Login_View(self, on_login=self.handle_login, on_cancel=self.handle_cancel)
        self.login_view.pack(fill="both", expand=True)

    def handle_login(self, email: str, password: str):
        # Placeholder de autenticação
        print(f"[login] email={email} senha={'*' * len(password)}")
        # Exemplo: após autenticar, você pode trocar de tela aqui.

    def handle_cancel(self):
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
