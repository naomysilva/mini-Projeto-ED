from queue import Empty


class Queue:
    
    def __init__(self):
        self.fila = []
        
    def size(self):
        return len(self.fila)
               
    def empty(self):
        if self.size() == 0:
            print("Fila Vazia")
           
        else:
            print("Fila Não esta vazia")
            
    def push(self,item):
        self.fila.append(item)
        
    def remove(self):
        self.fila.pop(0)

    def peek(self):
        if self.empty == False:
           print("fila vazia")
        else:
            return len(self.fila)-1
        
    def __repr__(self) -> str:
        return f'Queue({self.fila}' 
        
node = Queue()
        
for valor in range(3):
    acao = input(f'quantidade ações e o valor do dia {valor+1}:').split()
    node.push(acao)
    
print(node) 
print(node.size())