def bubbleSort(nums: list[int]) -> list:
    numsLen = len(nums)
    
    for _ in nums:
        print(nums)
        sorted = True
        for i in range(numsLen - 1):
            if nums[i] > nums[i + 1]:
                sorted = False
                nums[i + 1], nums[i] = nums[i], nums[i + 1] 
        if sorted:
            return nums
   

bubbleSort([1,2,3,4,5,6,7])
    
    