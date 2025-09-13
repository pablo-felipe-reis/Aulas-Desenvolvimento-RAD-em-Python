#acessar o arquivo aula1.py
#e manipular o arquivo dados1.txt
import os 

arquivo1 = open("dados1.txt", "w", encoding="utf-8")  # Modo escrita (sobrescreve)

print(os.path.abspath(arquivo1.name))

#arquivo2 = open("d:Onedrive/yduuqs/python/")
#                "maniopulação de dados/exemplo/dadps1.txt")
arquivo1.write("Ola, mundo!\n")

print(os.path.relpath(arquivo1.name))
print(arquivo1)

arquivo1.close()