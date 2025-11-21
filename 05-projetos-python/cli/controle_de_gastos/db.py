import sqlite3

def conectar_banco():
    conn = sqlite3.connect('gastos.db')
    return conn

def criar_tabela():
    conn = conectar_banco()
    c = conn.cursor()
    c.execute(''' CREATE TABLE IF NOT EXISTS gastos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    valor REAL NOT NULL)''')
    conn.commit()
    conn.close()

def adicionar_gasto_db(descricao, valor):
    conn = conectar_banco()
    c = conn.cursor()
    c.execute("INSERT INTO gastos (descricao, valor) VALUES (?,?)", (descricao, valor))
    conn.commit()
    conn.close()

def listar_gastos():
    conn = conectar_banco()
    c = conn.cursor()
    c.execute("SELECT * FROM gastos")
    gastos = c.fetchall()
    conn.close()
    for gasto in gastos:
        print(gasto)
    
def deletar_gastos():
    id_gasto = int(input("Digite o ID do produto que quer deletar: "))

    conn = conectar_banco()
    c = conn.cursor()
    c.execute("DELETE FROM gastos WHERE id = ?", (id_gasto,))
    conn.commit()
    conn.close()

    print(f"Gasto com ID {id_gasto} deletado com sucesso!")