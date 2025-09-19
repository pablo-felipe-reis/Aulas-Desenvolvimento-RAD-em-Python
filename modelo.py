class Pessoa:
    def __init__(self, cpf, nome, data_nascimento, oculos):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.oculos = oculos
    
    def __str__(self):
        return f"Pessoa(cpf={self.cpf}, nome='{self.nome}', data_nascimento='{self.data_nascimento}', oculos={self.oculos})"

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def __str__(self):
        return f"Veiculo(marca='{self.marca}', modelo='{self.modelo}', ano={self.ano})"
