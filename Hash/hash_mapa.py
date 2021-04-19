#criando tabela hash do tipo abstrato, utilizando dicionário
#Permite quando há colisão de key ele substitui o data
#Matheus Moreira dos Santos
#matheusms.eng@gmail.com

class HashTable:
    def __init__(self):
        self.size=11
        self.slots=[None] * self.size #lista que armazena os valores
        self.data=[None] * self.size

    def hashfunction(self, key, size): #implementação do metodo do resto
        return key%size#verificar se roda sem o size

    def rehash(self, oldhash, size):#função para rodar ate aparecer um slot vazio
        return (oldhash+1)%size

    def put(self, key, data): #pressupondo que algum momento havera entrada vazia
        hashvalue = self.hashfunction(key,len(self.slots))#recebe o valor da key

        if self.slots[hashvalue] == None: #verificando se hashvalue é um slot vazio
            #se estiver vazio armazena a key e a data
            self.slots[hashvalue] = key 
            self.data[hashvalue] = data

        else:
            #caso não esteja vazio e a chave for a mesma ele substitui a data 
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data #substituindo o data antigo

            else: #aplicando rehash ate achar um slot vazio
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key: #procurando um slot vazio e sem a chave
                    nextslot = self.rehash(hashvalue, len(self.slots))
                
                #colocando em um slot vazio
                if self.slots[nextslot] == None: 
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                
                else: #substitui caso ache a mesma chave
                    self.data[nextslot] = data

    def get(self, key):#procurando um key
        startslot = self.hashfunction(key, len(self.slots))
        data = None 
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key: #verifica se esta na posição inicial
                found = True
                data = self.data[position]
            else: 
                position=self.rehash(position, len(self.slots))#procurando pelos proximos slots ate achar
                if position == startslot:
                    stop = True #pausa quando acha o data da posição
            return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)    

'''
H=HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H[54])

'''
 
    

    
