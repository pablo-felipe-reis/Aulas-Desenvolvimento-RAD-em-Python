#Utilizando a Função Rename 
import os
nome_antigo = "arquivo_antigo.txt"
nome_novo = "arquivo_novo.txt"
try:
    os.rename(nome_antigo, nome_novo)
    print(f"o arquivo {nome_antigo}foi renomeado para {nome_novo}.")
except FileNotFoundError:
    print(f"o arquivo {nome_antigo}nã0 foi encontrado.")
except Exception as e:
    print(f"ocorreu um errro ao renomear o arquivo:{e}")
    
