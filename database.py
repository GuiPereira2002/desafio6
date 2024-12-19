import sqlite3

def get_db_connection():
    connection = sqlite3.connect("banco.sqlite")
    connection.row_factory = sqlite3.Row  # Para retornar resultados como dicionários
    return connection

def init_db():
    with get_db_connection() as conn:
        with open("schema.sql") as f:
            conn.executescript(f.read())
        conn.commit()
