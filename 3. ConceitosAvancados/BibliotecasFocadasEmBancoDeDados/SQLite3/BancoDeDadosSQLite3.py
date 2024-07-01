'''
SQLite é um sistema de gerenciamento de banco de dados relacional leve 
e amplamente utilizado, e no python, a
biblioteca padrão para interagir com bancos de dados SQLite é a sqlite3.
 '''
import sqlite3

#1. Conectar ao Banco de Dados
#Conectar e Criar um Banco de Dados


# Conectar ao banco de dados (se não existir, será criado)
conexao = sqlite3.connect('exemplo.db')

# Fechar a conexão
conexao.close()


#2. Executar Consultas SQL
#Criar Tabelas


conexao = sqlite3.connect('exemplo.db')
cursor = conexao.cursor()

# Criar uma tabela
cursor.execute('''CREATE TABLE usuarios
                  (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER)''')

conexao.commit()

# Fechar a conexão
conexao.close()

#Inserir Dados

conexao = sqlite3.connect('exemplo.db')
cursor = conexao.cursor()

# Inserir dados
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('João', 30)")

conexao.commit()

# Fechar a conexão
conexao.close()

#Consultar Dados

conexao = sqlite3.connect('exemplo.db')
cursor = conexao.cursor()

# Consultar dados
cursor.execute("SELECT * FROM usuarios")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Fechar a conexão
conexao.close()

# Atualizar Dados

conexao = sqlite3.connect('exemplo.db')
cursor = conexao.cursor()

# Atualizar dados
cursor.execute("UPDATE usuarios SET idade = 31 WHERE nome = 'João'")

conexao.commit()

# Fechar a conexão
conexao.close()

#Deletar Dados

conexao = sqlite3.connect('exemplo.db')
cursor = conexao.cursor()

# Deletar dados
cursor.execute("DELETE FROM usuarios WHERE nome = 'João'")

conexao.commit()

# Fechar a conexão
conexao.close()

# 3. Parâmetros e Consultas Seguras
# Uso de Parâmetros

conexao = sqlite3.connect('exemplo.db')
cursor = conexao.cursor()

# Uso de parâmetros
nome = 'Maria'
idade = 28
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", (nome, idade))

conexao.commit()

# Fechar a conexão
conexao.close()

# 4. Transações
# Início e Commit de Transações

conexao = sqlite3.connect('exemplo.db')
cursor = conexao.cursor()

try:
    cursor.execute("BEGIN")
    cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Carlos', 25)")
    cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Ana', 22)")
    cursor.execute("COMMIT")
except sqlite3.Error as e:
    print("Erro durante a transação:", e)
    conexao.rollback()

conexao.close()

# 5. Consultas Avançadas
# Joins

conexao = sqlite3.connect('exemplo.db')
cursor = conexao.cursor()

cursor.execute('''SELECT usuarios.nome, pedidos.produto
                  FROM usuarios
                  INNER JOIN pedidos ON usuarios.id = pedidos.usuario_id''')
rows = cursor.fetchall()

for row in rows:
    print(row)

conexao.close()

# Group By e Having

conexao = sqlite3.connect('exemplo.db')
cursor = conexao.cursor()

cursor.execute('''SELECT produto, COUNT(*)
                  FROM pedidos
                  GROUP BY produto
                  HAVING COUNT(*) > 1''')
rows = cursor.fetchall()

for row in rows:
    print(row)

conexao.close()

# 6. Gerenciamento de Transações e Exceções
# Tratamento de Exceções

conexao = sqlite3.connect('exemplo.db')
cursor = conexao.cursor()

try:
    cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('Fernanda', 'xyz')")
    conexao.commit()
except sqlite3.Error as e:
    print("Erro durante a inserção:", e)
    conexao.rollback()

conexao.close()

# 7. Utilização de Context Manager (with)
# Uso de with para Gerenciamento de Conexão

# O uso do with garante que a conexão será fechada corretamente após o bloco de código
with sqlite3.connect('exemplo.db') as conexao:
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

# 8. Funções Específicas do SQLite
# Funções SQLite no SQL

conexao = sqlite3.connect(':memory:')  # Banco de dados em memória

# Uso de funções SQLite no SQL
cursor = conexao.cursor()
cursor.execute("SELECT nome, UPPER(nome) FROM usuarios")
rows = cursor.fetchall()

for row in rows:
    print(row)

conexao.close()

# 9. Backup e Restauração de Banco de Dados
# Backup

import shutil

# Conectar ao banco de dados
conexao = sqlite3.connect('exemplo.db')

# Realizar backup
shutil.copyfile('exemplo.db', 'backup_exemplo.db')

# Fechar a conexão
conexao.close()

# Restauração

import shutil

# Restaurar backup
shutil.copyfile('backup_exemplo.db', 'exemplo.db')

# 10. Criação de Índices
# Criação de Índices

conexao = sqlite3.connect('exemplo.db')
cursor = conexao.cursor()

cursor.execute("CREATE INDEX idx_nome ON usuarios (nome)")

conexao.commit()
conexao.close()

# 11. Trabalho com Datas
# Uso de Datas

import datetime

conexao = sqlite3.connect('exemplo.db')
cursor = conexao.cursor()

data_atual = datetime.date.today()
cursor.execute("INSERT INTO logs (data, mensagem) VALUES (?, ?)", (data_atual, 'Erro de sistema'))

conexao.commit()
conexao.close()

# 12. Utilização de Chaves Estrangeiras
# Chaves Estrangeiras

conexao = sqlite3.connect('exemplo.db')
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE usuarios (
                  id INTEGER PRIMARY KEY,
                  nome TEXT,
                  idade INTEGER)''')

cursor.execute('''CREATE TABLE pedidos (
                  id INTEGER PRIMARY KEY,
                  usuario_id INTEGER,
                  produto TEXT,
                  FOREIGN KEY (usuario_id) REFERENCES usuarios (id))''')

conexao.commit()
conexao.close()