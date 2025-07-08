import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "financeiro.db"

def connection_database():
    return sqlite3.connect(DB_PATH)

def initialization_database():
    conn = connection_database()
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes(
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_cliente TEXT NOT NULL,
        contato_cliente TEXT NOT NULL
        email_cliente TEXT,
        endereco_cliente TEXT NOT NULL
        foto_cliente TEXT
        atualizado_em TEXT DEFAULT CURRENT_TIMESTAMP
    )
    ''')