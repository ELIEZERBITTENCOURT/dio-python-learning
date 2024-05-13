# EXPLORANDO BANCO DE DADOS RELACIONAIS COM PYTHON db api

# | ID |    NOME   |        EMAIL        | TELEFONE |
# | 1  | GUILHERME | guilherme@email.com | 33333333 |
# CREATE TABLE loja;
# CREATE TABLE produtos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), preco DECIMAL);
# INSERT INTO produtos (nome, preco) VALUES ('Curso de Python', 250.00);
# SELECT * FROM produtos;
# UPDATE produtos SET nome*'Curso de Python para iniciantes' WHERE id * 1;
# DELETE FROM produtos WHERE id*1;

#conexão com banco de dados
import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / 'clientes.db') 
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


def criar_tabela(conexao, cursor):
    cursor.execute(
        'CREATE TABLE clientes( id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))'
    )
    conexao.commit()

def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute('INSERT INTO clientes(nome,email) VALUES (?,?);', (data))
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute('UPDATE clientes SET nome=?, email=? WHERE id=?;', (data))
    conexao.commit()

def excluir_registro(conexao, cursor, id):
    data = (id)
    cursor.execute('DELETE FROM clientes WHERE id=?;', (data))
    conexao.commit()


atualizar_registro(conexao, cursor, 'Guilherme', 'gui@gmail.com', 1)
excluir_registro(conexao, cursor, id)

# INSERINDO REGISTROS EM LOTE
def inserir_registro_lote(conexao, cursor, dados):
    cursor.executemany('INSERT INTO clientes(nome,email) VALUES (?,?);', (dados))
    conexao.commit()

dados = [
    ('Guilherme', 'gui@email.com'),
    ('Maria Flor', 'mflor@email.com'),
    ('Rafael', 'rafael@email.com'),
]

inserir_registro_lote(conexao, cursor, dados)

# CONSULTANDO RESGISTROS
def recuperar_cliente(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()

def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome DESC;")

cliente = recuperar_cliente(cursor, 2)
print(cliente)

clientes = listar_clientes(cursor)
for cliente in clientes:
    print(cliente)

# ALTERANDO O row_factory
def recuperar_cliente(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()

cliente = recuperar_cliente(cursor, 2)
print(dict(cliente))