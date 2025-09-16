#utilizando a funçãon Remove 
import os 
arquivo_a_remover = "arquivo_a_remover.txt"
try:
    os.remove(arquivo_a_remover)
    print(f"o arquivo{arquivo_a_remover} foi removido com sucesso.")
except FileNotFoundError:
    print(f"o arquivo{arquivo_a_remover}não foui encontrado.")
except Exception as e :
    print(f"ocorreu um erro ao remover o arquivo :{e}")
    