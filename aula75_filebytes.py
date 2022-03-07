"""
    Permite que sejam criados pacotes de bytes
"""
    


import struct

nome = 'Lucas'
idade = 23
altura = 1.73


#encode tranforma meu nome para uma string 
cod = struct.pack('5s I f', nome.encode(), idade, altura)

print(cod)

#Criei meu arquivo no formato codificado com pacotes de bytes
arq = open('pessoa.cod', 'wb')
arq.write(cod)

arq.close()

arq = open('pessoa.cod', 'rb')
cod_ab = arq.readline()

print(cod_ab)

#Agora para desempacotar a minha codificação

cod_desemp = struct.unpack('5s I f', cod_ab)

print(cod_desemp)


print(cod_desemp[0].decode())


#Para facilitar a nossa vida podemos utilizar uma tupla

t = (b'joao', 23, 1.68)

s = struct.Struct('4s I f')


data = s.pack(*t)

print(data)


