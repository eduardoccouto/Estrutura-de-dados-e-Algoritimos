def binarySearch(nums, n):
    esquerda = 0
    direita = len(nums)
    
    while direita > esquerda:
        mid  = int((esquerda + direita) / 2)
        
        if nums[mid] == n:
            return n, mid
        elif nums[mid] > n:
            direita = mid
        else:
            esquerda = mid
    return -1       

print(binarySearch([1,2,3,4,5,6,7,8,9,10], 7)) 