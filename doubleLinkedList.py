class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def adiciona_inicio(self, value):
        new_node = Node(value)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
             
        self.head = new_node 
        
    def adiciona_final(self, value):
        new_node = Node(value)
        new_node.prev = self.tail
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        
        self.tail = new_node  
        
    def remove_do_comeco(self):
        if self.head is None:
            return []
        
        pointer = self.head.value
        
        self.head = self.head.next
        
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
            
        return pointer
            
            
            
                
            
        
            
            
        