#exemplo de leitura de arquivo
#abrindo o arquivo no modo leitura
import os 

arquivo = open('exemplo.txt', 'r', encoding='utf-8')  #'r' para leitura
conteudo = arquivo.read()
print('tipo do conteudo:', type(conteudo))  
print('conteudo retornado pelo read:')
print(repr(conteudo))
arquivo.close()