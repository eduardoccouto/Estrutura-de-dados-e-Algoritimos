def quicksort(array, left, right):
    if left < right:
        print(array[left: right +1])        
        pi = particion(array, left, right)
        quicksort(array, left, pi - 1)
        quicksort(array, pi + 1, right)
        
def particion(array, left, right):
    pivot = array[right]
    i = left - 1 
    
    for j in range(left, right):
        
        if array[j] <= pivot:
            i += 1
            
            array[j], array[i] = array[i] , array[j]
            
    array[i+1], array[right] = array[right], array[i+1] 
    
    return i + 1


arr = [0,8,9,6,7,4,1,20,75,18,30]

quicksort(arr, 0, len(arr) -1)

         
            
            
            
        
    
            
    
           
        