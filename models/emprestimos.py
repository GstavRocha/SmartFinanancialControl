import sys
from pathlib import Path

# Adiciona o diretório raiz ao sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from Database_Manager import Database_Manager
from models.query_util import Query_Util
from models.DAO_utils import BaseDAO

class EmprestimosDAO:
    def __init__(self):
        db = Database_Manager()
        query = Query_Util(db)
        super().__init__(
            table_name="emprestimos",
            primary_key="id_emprestimos",
            query_util=query
        )