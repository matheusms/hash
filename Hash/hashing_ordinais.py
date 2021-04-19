#hashing de uma string usando valores ordnais
# criando um espalhamento de hashing através da soma dos caracteres ordenados da string

def hash(astring, tablesize):#recebe valor de uma string e o tamanho da tabela
    sum = 0
    for pos in range(len(astring)):
        #para cada letra pega sua ordem nos ordinários e soma todos
        sum = sum + ord(astring[pos])
    #retorna o resto da soma dos ord pelo tamanho da tabela
    return sum%tablesize

#apenas testando
h = hash('matheusmoreira', 11)
#posição retorna a posição em que deve ser colocado na tabela
print(h)

#anagramas recebem mesma posição CUIDADO