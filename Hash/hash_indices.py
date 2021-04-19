#hashing simples de expalhamento por indices
#Matheus Moreira dos Santos
#matheusms.eng@gmail.com

def hash(indice, tablesize):#recebe valor do indice e o tamanho da tabela
    #a posição na tabela é o resto da divisão do indice pelo tamanho da tabela
    return indice%tablesize

#apenas testando
h = hash(130, 13)
#posição retorna a posição em que deve ser colocado na tabela
print(h)