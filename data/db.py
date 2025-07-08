import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "data"/ "financeiro.db"

def connection_database():
    return sqlite3.connect(DB_PATH)