import os
#abrindo o arquuivo no modo escrita 
arquivo= open('exemplo.txt', 'w', encoding='utf-8')
            
#exibindo os atributos do arquivo

print("nome do arquivo:", arquivo.name)
print("modo de abertura:", arquivo.mode)
print("arquivo está fechado?", arquivo.closed)

#escrevendo no arquivo
arquivo.write("Olá, mundo!\n")


#fechando o arquivo 

arquivo.close()

#verificando se o arquivo está fechado

print("arquivo está fechado agora?",arquivo.closed)


#exibindo caminhos relatico e absoluto 

realpath = os.path.realpath('exemplo.txt')
abspath = os.path.abspath('exemplo.txt')

print("Caminho relativo:",realpath)
print("Caminho absoluto:",abspath)
