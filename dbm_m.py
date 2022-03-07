import dbm
import struct

#c->create or open if already exists

#database você lida como se fosse um dicionario

db = dbm.open('contatos.db', 'c')

#Automaticamente converte pro formato de bytes
#Praticamente só armazena strings
db['pedro'] = 'pedro_henrique53@gmail.com'


#print(db['pedro'])

db['joao'] = str(13)


print(len(db))

#Podemos acessar as chaves 


print(db.keys())

#Podemos deletar uma chave

del db['joao']

#Podemos percorrer as chaves usando um for loop

for k in db.keys():
    print(k)
    
#Podemos dar um pop em db['joao']

db['joao'] = 'joao'

db.pop('joao')


#Conseguimos empacotar nossos valores



db['ana'] = struct.pack('I', 21)
print(db['ana'])