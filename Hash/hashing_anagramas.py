#hashing de uma string usando valores ordnais com pesos
#para utilizar em anagramads podemos utilizar o valor da 'pos' do caractere como peso na soma de cada item
#Matheus Moreira dos Santos
#matheusms.eng@gmail.com

def hash(astring, tablesize):#recebe valor de uma string e o tamanho da tabela
    sum = 0
    
    for pos in range(len(astring)):
        #para cada letra pega sua ordem nos ordinários e soma todos multiplicando pela sua posição na string  (pos+1 para nao ter 0)            
        sum = sum + ord(astring[pos])*(pos+1)
    #retorna o resto da soma dos ord pelo tamanho da tabela
    return sum%tablesize

#apenas testando
h = hash('cat', 11)
#posição retorna a posição em que deve ser colocado na tabela
print(h)