#Manipulação de string 

arquivo =open ('dados1.txt','r',encoding= 'utf-8')
conteudo = arquivo.read()
print ("tipo de conteudo : ",type(conteudo))
print('conteudo retormado pelo read:')
print(repr(conteudo))
arquivo.close()