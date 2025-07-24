import sqlite3
from pathlib import Path

class Database_Manager:
    def __init__(self, dbname= "financeiro.db"):
        self.db_path = Path(__file__).parent / "data" /dbname
        self.conn = sqlite3.connect(str(self.db_path))
        self.cursor = self.conn.cursor()
    def _connect(self):
        print("estabelecendo conexao")
        self.conn = sqlite3.connect(str(self.db_path))
        self.cursor = self.conn.cursor()
        print("conexao estabelecida")
    
    def reconnect(self):
        if self.conn:
            self.conn.close()
        self._connect()
        
    def inicializar_tabelas(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_cliente TEXT NOT NULL,
            contato_cliente TEXT NOT NULL,
            email_cliente TEXT,
            endereco_cliente TEXT NOT NULL,
            foto_cliente TEXT,
            atualizado_em TEXT DEFAULT CURRENT_TIMESTAMP
        );
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS emprestimos (
            id_emprestimos INTEGER PRIMARY KEY AUTOINCREMENT,
            id_cliente INTEGER NOT NULL,
            valor_principal REAL NOT NULL,
            juros_mensal REAL NOT NULL,
            data_emprestimo DATE,
            numero_parcelas INTEGER,
            status TEXT NOT NULL CHECK (status IN ('ativo', 'quitado', 'atrasado')),
            CONSTRAINT fk_clientes_emprestimo FOREIGN KEY (id_cliente)
                REFERENCES clientes(id_cliente)
                ON DELETE CASCADE
        );
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS parcelas (
            id_parcelas INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_emprestimo INTEGER NOT NULL,
            valor_parcela REAL NOT NULL,
            data_vencimento DATE NOT NULL,
            data_pagamento DATE,
            status TEXT NOT NULL CHECK (status IN ('pendente', 'pago', 'atrasado')),
            id_emprestimo INTEGER NOT NULL,
            CONSTRAINT fk_parcelas_emprestimo FOREIGN KEY (id_emprestimo)
                REFERENCES emprestimos(id_emprestimos)
                ON DELETE CASCADE
        );
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS pagamentos (
            id_pagamentos INTEGER PRIMARY KEY AUTOINCREMENT,
            id_parcelas INTEGER NOT NULL,
            valor_pago REAL NOT NULL,
            data_pagamento TEXT NOT NULL,
            observacao TEXT,
            CONSTRAINT fk_pagamentos_parcelas FOREIGN KEY (id_parcelas)
                REFERENCES parcelas(id_parcelas)
                ON DELETE CASCADE
        );
        ''')

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id_usuarios INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        );
        ''')

        self.conn.commit()

    def close(self):
        self.conn.close()
        