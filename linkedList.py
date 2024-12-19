class Data:
    def __init__(self, value):
       self.value =  value
       self.next = None

class Node:
    
    def __init__(self):
        self.head = None
    
    def append(self, valor):
        if self.head == None:
            self.head = Data(valor)
            return 
        else:
            atual = self.head
            while atual.next:
                atual = atual.next
                
            atual.next = Data(valor)
            return 
        
        
    
            
       
        
            
        
                    




        
