from linkedList import Node, Data



def encontraMeio(head):
    midle = head
    fast = head.next
    
    while fast and fast.next:
        midle = midle.next
        fast = fast.next.next
        
    return midle

def merge(l1, l2):
    head = Data()
    tail = head

    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
            
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
        
    tail.next = l1 or l2
    return head.next


def mergeSort(head):
    if not head or not head.next:
        return head
    
    middle = encontraMeio(head)
    afterMiddle = middle.next
    middle.next = None
    
    left = mergeSort(head)
    right = mergeSort(afterMiddle)
    
    sortedList = merge(left, right)
    
    return sortedList
    
    


list = Node()


list.append(25)
list.append(2)
list.append(10)
list.append(8)
list.append(4)


#mergeSort(list.head)
list.mostrarLista()
pointer = list.head
        
while pointer:
    print(pointer.value)
    
    pointer = pointer.next








    