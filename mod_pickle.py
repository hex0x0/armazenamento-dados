#eu amor o pickle



import pickle



arq = open('arquivo.pck', 'wb')

l1 = [1, 2, 3]

pickle.dump(l1, arq)


class Pessoa():
    def __init__(self, n, p):
        self.n = n 
        self.p = p
        
    def ola(self):
        print('Ola sou %s e peso %s'%(self.n, self.p))
        
        

Pedro = Pessoa('Pedro', 75)

pickle.dump(Pedro, arq)

arq.close()

arq = open('arquivo.pck', 'rb') #escrever objetos que nós criamos para arquivos

x = pickle.load(arq)

print(x)

y = pickle.load(arq)


y.ola()

z = pickle.dumps(y)



