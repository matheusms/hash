#tabela hash evitando colisões simples

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
            print(pos)
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
        return self.tab
        '''
        for i in self.tab:
            #print("Hash [%d] = " %i, end="")
            #print(self.tab[i])'''

    def func_Hash(self, key):#dando entrada na tabela com os valores
        
        return key%self.size #retorna o valor da posiçao para adicionar na tabela


tab = Hash(11)
x='s'
x=x.upper()
while (x=='S'):
    valor=int(input('insira um item(numeros inteiros): '))
    tab.insere(valor)
    x=input("continuar? (S/N)")
    x=x.upper()

print(tab.imprime())


