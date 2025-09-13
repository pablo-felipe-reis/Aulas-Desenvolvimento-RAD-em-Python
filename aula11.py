frase= "Eu amo comer amoras no café da manhã"

#Resultado obtido utilizando o metódo count diretamente 
print("contagem direta:",frase.count('amo'))

#Resultado obtidon utilizando a quebra de frase em palavras 
contador =0
lista_termos = frase.split()
for termo in lista_termos:
    if termo == 'amo':
        contador +=1
        print ("Contagem correta:",contador)
    