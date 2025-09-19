import sqlite3 as conector
from modelo import Pessoa

# Abertura de conexão e aquisição de cursor
conexao = conector.connect("./meu_banco.db")
cursor = conexao.cursor()

# Criação de um objeto do tipo Pessoa
pessoa = Pessoa(30000000099, 'Silva', '1990-03-30', False)

# Definição de um comando com named parameter
comando = '''INSERT INTO Pessoa 
VALUES (:cpf,:nome,:data_nascimento,:oculos);'''
cursor.execute(comando, {"cpf":pessoa.cpf,
                        "nome":pessoa.nome,
                        "data_nascimento":pessoa.data_nascimento,
                        "oculos":pessoa.oculos})
# Efetivação do comando
conexao.commit()

# Fechamento das conexões
cursor.close()
conexao.close()
