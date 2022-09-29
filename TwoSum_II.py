# Two Sum II Leetcode 167

def twoSum(self, numbers: List[int], target: int) -> List[int]:
    start, end = 0, len(numbers) - 1
    n = len(int)
    
    while start < end:
        
        curSum = numbers[start] + numbers[end]
        
        if curSum > target:
            end -= 1
        elif curSum < target:
            start += 1
        else:
            return [start + 1, end + 1]          
        
