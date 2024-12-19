class BadSolution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        
        for i in range(len(nums)):
            for j in range(i):
                
                if nums[i] == nums[j] and i != j:
                    count = i - j
                    if count <= k:
                        return True
                    
        return False

def containsNearbyDuplicate(nums, k):
    
    d = {}

    for idx, x in enumerate(nums):
        if x in d and abs(idx - d[x] ) <= k:
                return True
        else:
            d[x] = idx

    return False



containsNearbyDuplicate([1,2,3,1], 3)