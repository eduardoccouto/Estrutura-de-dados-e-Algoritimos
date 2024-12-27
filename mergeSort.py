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
    
    
# class Node:
#     def __init__(self, value = 0 , next = None):
#         self.value = value
#         self.next = next

# node1 = Node(5)        
# node2 = Node(10, node1)        
# node3 = Node(2, node2)        
# node4 = Node(25, node3)        

# my_list = mergeSort(node4)
# print(my_list)
# list = Node()
list = Node()

list.append(25)
list.append(2)
list.append(10)
list.append(8)
list.append(4)


my_list = mergeSort(list.head)
print(my_list.next)

pointer = my_list.next
        
while pointer:
    print(pointer.value)
    
    pointer = pointer.next








    