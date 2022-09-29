# Two Sum
# Opposite Direction Two-Pointer

def twoSum(self, nums: List[int], target: int) -> List[int]:
    
    l, r = 0, len(nums) - 1
    
    while l < r:
        
        curSum = nums[l] + nums[r]
        
        if curSum > target:
            r -= 1
        
        elif curSum < target:
            r += 1
        
        else:
            return nums
