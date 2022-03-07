import struct


pessoas = {}
nome = 'lucas'
pessoas[nome] = {}




num_char = len(nome)

def passaPessoas(pessoas):

    pessoas['rg'] = 342342
    
    

def passaCpf(pessoas):
    pessoas['cpf'] = 3243
    
    
passaPessoas(pessoas[nome])
passaCpf(pessoas[nome])

#print(pessoas)


arq = open('lenha.cod', 'wb')



num_data = struct.pack('I', num_char)

#print(num_data)

arq.write(num_data)

arq.write(b'\n')


info = struct.pack('%is Q Q'%num_char, nome.encode(), pessoas[nome]['rg'], pessoas[nome]['cpf'])

arq.write(info)

arq.write(b'\n')

arq.close()


#agora abrir os dados

pessoasNovo = {}

try:
    arq = open('lenha.cod', 'rb')
    
    for num_char_nome in arq:
       
        num_char_nome = num_char_nome.split(b'\n')[0]
        
        decode = '%is Q Q'%struct.unpack('I', num_char_nome)
        
        #5s Q Q
        
        arqOutraLinha = arq.readline().split(b'\n')[0]
        
        
        info = struct.unpack(decode, arqOutraLinha)


        pessoas[info[0].decode()] = {'rg': info[1], 'cpf':info[2]} 
        
        
    print(pessoas)      

except IOError:
    {}
finally:
    print('Saindo aqui')
    
    
    


