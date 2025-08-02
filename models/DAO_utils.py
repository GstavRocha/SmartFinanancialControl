# from models.query_util import Query_Util
from models.query_util import Query_Util
class BaseDAO:
    def __init__(self, table_name, primary_key, query_util):
        self.table_name = table_name
        self.primary_key = primary_key
        self.query = query_util # Query_Util
    
    def get_all(self):
        return self.query.select_all(self.table_name)
    
    def get_by_id(self, id):
        return self.query.find_one(self.table_name, self.primary_key, id)
    
    def create(self, data: dict):
        return self.query.insert(self.table_name, data=data)
        