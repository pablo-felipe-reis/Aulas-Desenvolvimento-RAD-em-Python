# exemplo de leitura de arquivo
# abrindo o arquivo no modo leitura
import os 

arquivo = open('dados1.txt', 'r', encoding='utf-8')  # 'r' para leitura
conteudo = arquivo.readline()
print('tipo do conteudo:', type(conteudo))  
print('conteudo retornado pelo readline:')
print(repr(conteudo))
proximo_conteudo = arquivo.readline()
arquivo=open('exemplo.txt', 'r', encoding='utf-8')  # Reabrindo para ler o próximo conteúdo
print('próximo conteudo:', repr(proximo_conteudo))

print(repr(arquivo.readline()))  # Lê a próxima linha

arquivo.close()