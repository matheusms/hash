#tabela hash evitando colisões simples
#Matheus Moreira dos Santos
#matheusms.eng@gmail.com

class Hash:
    def __init__(self, sizetable):
        self.tab={}
        self.size=sizetable

    def cheia(self):#verificando se a tabela está cheia
        return len(self.tab)==self.size #se estiver cheia retorna true

    def insere(self, item):
        print('tamanho: ', self.size)
        if self.cheia():#conferindo se nao está cheia, se estiver cheia finaliza o inserir
            print('TABELA HASH CHEIA, AUMENTAR')
            return
        pos = self.func_Hash(item)
        if self.tab.get(pos) == None: #confere se a posição esta vazia
            #print(pos)
            self.tab[pos]=item
            print("inserido Hash[%d]" %pos)
        else: #se a posição estiver ocupada
            nextpos = self.rehash(pos, self.size)
            while self.tab.get(nextpos) != None: #procurando uma posição vazia atraves do rehash
                nextpos = self.rehash(nextpos, self.size) #nextpos armazena a posição para verificar
            self.tab[nextpos]=item
            print("inserido Hash[%d]" %nextpos)

    def rehash(self, oldhash, sizetable):
        return (oldhash+1)%sizetable

    def imprime(self):
        for i in self.tab:
            print("Hash[%d] = " %i, end="")
            print(self.tab[i])
    
    def func_Hash(self, key):#dando entrada na tabela com os valores           
        return key%self.size #retorna o valor da posiçao para adicionar na tabela
    
    def search(self, key):
        pos=self.func_Hash(key)
        if self.tab.get(pos) == None: #não tem nada nessa posição
            return -1
        elif self.tab[pos] == key: #se o item na posição é igual a chave encontramos
            return pos
        else: 
            nextpos = self.rehash(pos, self.size)
            while self.tab.get(nextpos) != None and self.tab.get(nextpos) != key: #realiza rehash até que encontre uma none ou a chave
                nextpos = self.rehash(nextpos, self.size)
                if nextpos == pos: #verifica se deu a volta inteira na tabela
                    return -1
            
            if self.tab.get(nextpos) != key or self.tab.get(nextpos) == None:#caso encontre um lugar vazio ou retorne pra mesma posição
                return -1
            elif self.tab.get(nextpos) == key: #salva a posição caso encontre
                pos = nextpos
                return pos
        return -1

    def apaga(self, key):
        pos = self.search(key)
        if pos == -1:#caso nao exista a chave
            print("Item não existe!")
        else: 
            del self.tab[pos]#apagando a chave
            print("Item apagado da posição %d" %pos)


tam=11
tab = Hash(tam)

print("Tabela HASH sem colisões (%d itens" %tam)
print("----------------------------------")

x='s'
x=x.upper()
while (x=='S'):
    valor=int(input('insira um item(numeros inteiros): '))
    tab.insere(valor)
    x=input("continuar? (S/N)")
    x=x.upper()
tab.imprime()

busca = int(input("\n Insira o valora buscar: "))
pos = tab.search(busca)

if pos == -1:
    print("Item não encontrado")
else: 
    print("Item encontrado, posição: ", pos)


ap = int(input("Qual valor deseja apagar? "))
pos = tab.apaga(ap)
tab.imprime()