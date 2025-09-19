import sqlite3 as conector
from modelo import Marca, Veiculo

conexao = conector.connect("./meu_banco.db")
conexao.execute("PRAGMA foreign_keys = on")
cursor = conexao.cursor()

# Inserção de dados na tabela Marca
comando1 = '''INSERT INTO Marca (nome, sigla) VALUES (:nome, :sigla);'''

marca1 = Marca("Marca A", "MA")
cursor.execute(comando1, {"nome": marca1.nome, "sigla": marca1.sigla})
marca1.id = cursor.lastrowid
print(f"Marca 1 inserida com ID: {marca1.id}")

marca2 = Marca("Marca B", "MB")
cursor.execute(comando1, {"nome": marca2.nome, "sigla": marca2.sigla})
marca2.id = cursor.lastrowid
print(f"Marca 2 inserida com ID: {marca2.id}")

# VERIFIQUE se as marcas existem na tabela
cursor.execute("SELECT * FROM Marca")
marcas_existentes = cursor.fetchall()
print("Marcas no banco:", marcas_existentes)

# Inserção de dados na tabela Veiculo
comando2 = '''INSERT INTO Veiculo VALUES (:placa, :ano, :cor, :motor, :proprietario, :marca);'''

veiculo1 = Veiculo("AAA0001", 2001, "Prata", 1.0, 10000000099, marca1.id)
veiculo2 = Veiculo("BAA0002", 2002, "Preto", 1.4, 10000000099, marca1.id)
veiculo3 = Veiculo("CAA0003", 2003, "Branco", 2.0, 20000000099, marca2.id)
veiculo4 = Veiculo("DAA0004", 2004, "Azul", 2.2, 30000000099, marca2.id)

print(f"Inserindo veículo 1 com marca ID: {veiculo1.marca}")
cursor.execute(comando2, vars(veiculo1))

print(f"Inserindo veículo 2 com marca ID: {veiculo2.marca}")
cursor.execute(comando2, vars(veiculo2))

print(f"Inserindo veículo 3 com marca ID: {veiculo3.marca}")
cursor.execute(comando2, vars(veiculo3))

print(f"Inserindo veículo 4 com marca ID: {veiculo4.marca}")
cursor.execute(comando2, vars(veiculo4))

conexao.commit()
cursor.close()
conexao.close()