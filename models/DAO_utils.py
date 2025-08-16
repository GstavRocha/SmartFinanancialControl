class BaseDAO:
    def __init__(self, table_name, primary_key, query_util):
        self.table_name = table_name
        self.primary_key = primary_key
        self.query = query_util

    # ----------------- CREATE -----------------
    def create(self, data: dict):
        """Cria um novo registro e retorna o ID."""
        return self.query.insert(self.table_name, data)

    # ----------------- READ -----------------
    def get_all(self):
        """Retorna todos os registros."""
        return self.query.select_all(self.table_name)

    def get_by_id(self, record_id):
        """Busca um registro pelo ID primário."""
        return self.query.find_one(self.table_name, self.primary_key, record_id)

    def find_by(self, column, value):
        """Busca registros por uma coluna específica."""
        return self.query.select_by(self.table_name, column, value)
    
    def find_a(self, show_column, where_column, value):
        return self.query.find_a_column(self.table_name, show_column, where_column,value)

    # ----------------- UPDATE -----------------
    def update(self, record_id, data: dict):
        """Atualiza um registro pelo ID."""
        return self.query.update(self.table_name, data, self.primary_key, record_id)

    # ----------------- DELETE -----------------
    def delete(self, record_id):
        """Remove um registro pelo ID."""
        return self.query.delete(self.table_name, self.primary_key, record_id)
