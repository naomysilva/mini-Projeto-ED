class FilaArray:
    
    CAPACIDADE_PADRAO = 10
    
    def __init__(self):
        self._dados = [[None]] * FilaArray.CAPACIDADE_PADRAO
        self._tamanho = 0
        self._inicio = 0
            
    def push(self,elem):
        disponivel = (self._inicio + self._tamanho) % len(self._dados)
        self._dados[disponivel] = elem
        self._tamanho += 1
        
    def pop(self):
        result = self._dados[self._inicio]
        self._dados[self._inicio] = None
        self._inicio = (self._inicio + 1) % len(self._dados)
        self._tamanho -= 1
        return result
                
    
    def comprarAcao(self):
        quatidadeAcao,valor =input("Comprar acção: \n Quantidade e Valor").split()
        
        adicionarComprarACao =[int(quatidadeAcao),int(valor)]
        
        self.push(adicionarComprarACao)

        
    def venderAcao():
        pass
    
    def desfazerOperacao():
        pass
            

           
    def transicoes(self):
        while(True):
            escolha = int(input("Seja bem-vindx escolha uma das operações abaixo: \n 1-comprar ação(ões) \n 2-vender ação(ões) \n 3-Desfazer Operação Anterior \n 4-Sair \n"))
            if escolha == 1:
                self.comprarAcao()
            elif escolha == 2:
                self.venderAcao()
            elif escolha == 3:
                self.desfazerOperacao()
            elif escolha == 4:
                break
            else:
                print("Operação invalida")
                
            
    def __len__(self):
        return self._tamanho

    def is_empty(self):
        return self._tamanho == 0
        
    def __str__(self):
        posicao = self._inicio
        result = "Quantidade Ação:"
        for k in range(self._tamanho):
            result += str(self._dados[0])
        return result

lista = FilaArray()

lista.transicoes()

print(lista)
