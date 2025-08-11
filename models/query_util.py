# from Database_Manager import Database_Manager

class Query_Util:
    def __init__(self, db_manager):
        self.db = db_manager
        self.db.inicializar_tabelas()

    # ----------------- SELECT -----------------
    def select_all(self, table):
        self.db.connect()
        self.db.cursor.execute(f"SELECT * FROM {table};")
        rows = self.db.cursor.fetchall()
        return [dict(row) for row in rows]

    def select_by(self, table, column, value):
        self.db.connect()
        sql = f"SELECT * FROM {table} WHERE {column} = ?;"
        self.db.cursor.execute(sql, (value,))
        rows = self.db.cursor.fetchall()
        return [dict(row) for row in rows]

    def find_one(self, table, column, value):
        self.db.connect()
        sql = f"SELECT * FROM {table} WHERE {column} = ? LIMIT 1;"
        self.db.cursor.execute(sql, (value,))
        row = self.db.cursor.fetchone()
        return dict(row) if row else None
    
    def find_a_column(self, table, show_column, where_column, value):
        self.db.connect()
        sql = f"SELECT {show_column} from {table} WHERE {where_column} = ? LIMIT 1;"
        self.db.cursor.execute(sql, (value,))
        row = self.db.cursor.fetchone()
        return dict(row) if row else None

    # ----------------- INSERT -----------------
    def insert(self, table, data: dict):
        """
        Insere registro baseado em um dicionário.
        Exemplo:
            query.insert("clientes", {
                "nome_cliente": "João",
                "contato_cliente": "99999-9999",
                "email_cliente": "joao@email.com"
            })
        """
        self.db.connect()
        columns = ",".join(data.keys())
        placeholders = ",".join(["?"] * len(data))
        sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        self.db.cursor.execute(sql, tuple(data.values()))
        self.db.conn.commit()
        return self.db.cursor.lastrowid

    # ----------------- UPDATE -----------------
    def update(self, table, data: dict, where_column, where_value):
        """
        Atualiza registro baseado em um dicionário.
        Exemplo:
            query.update("clientes",
                {"nome_cliente": "Carlos", "contato_cliente": "77777-7777"},
                "id_cliente",
                1
            )
        """
        self.db.connect()
        set_clause = ", ".join([f"{col} = ?" for col in data.keys()])
        sql = f"UPDATE {table} SET {set_clause} WHERE {where_column} = ?"
        self.db.cursor.execute(sql, tuple(data.values()) + (where_value,))
        self.db.conn.commit()
        return self.db.cursor.rowcount

    # ----------------- DELETE -----------------
    def delete(self, table, where_column, where_value):
        self.db.connect()
        sql = f"DELETE FROM {table} WHERE {where_column} = ?"
        self.db.cursor.execute(sql, (where_value,))
        self.db.conn.commit()
        return self.db.cursor.rowcount