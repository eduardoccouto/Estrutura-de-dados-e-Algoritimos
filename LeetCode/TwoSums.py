def twoSum(nums, target):
    hasher = {}
    for idx, i in enumerate(nums): #posição, valor
        if hasher.get(i) is not None:   #se a chave não for vazia, retorna  
            return[hasher.get(i), idx]
        hasher[target-i] = idx #armazena a chave sendo {target - valor : indice}
        
list = [4,7,9,2,3,10,8]
target = 19

twoSum(list, target)