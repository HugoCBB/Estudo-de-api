import sqlite3

conn = sqlite3.connect('meu_banco.db')
cursor = conn.cursor()

def criar_tabela():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuario(
        id  INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        idade INTEGER,
        cep INTEGER,
        bairro TEXT,
        localidade TEXT,
        estado TEXT,
        regiao TEXT
                   
    )''')

    
    

def adicionar_dados(nome, idade, cep, bairro, localidade, estado, regiao):
    conn.execute("INSERT INTO usuario (nome, idade, cep, bairro, localidade, estado, regiao) VALUES (?, ?, ?, ?, ?,?,?)", (nome, idade, cep, bairro, localidade, estado, regiao))
    conn.commit()


def deletar_dados():

