#contador de string
with open ('dados1.txt',encoding='utf-8')as arquivo:
    texto =arquivo.read()
    contador =texto.count("olá")
    print ("total de olás",contador)