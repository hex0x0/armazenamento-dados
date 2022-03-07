import json

#Criar um objeto qualquer

data = {'Nome':'Pedro', 'RG':2718080, 'CPF':344}

file  = open('teste.json', 'wb')

data_string = json.dumps(data)




file.write(data_string.encode())


file.close()

file = open('teste.json', 'ab')

data = [1, 2, 3, 4]


data_s = json.dumps(data)

file.write(data_s.encode())


data = ('a', 'b', 'c')
#retorna uma lista no lugar
#json não aceita tuplas

file =open('teste.json', 'rb')


data_total = file.readline()

print(data_total)

data1 = data_total[:44]

#print(data1)

obj1 = json.loads(data1)

print(obj1)

data2 = data_total[44:56]

obj2 = json.loads(data2)

print(obj2)


class Pessoa():
    pass



a = Pessoa()

print(a.__dict__)
