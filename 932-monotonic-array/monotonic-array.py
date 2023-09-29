class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = True
        i = 1
        
        while i < len(nums):
            if nums[i] < nums[i - 1]:
                increasing = False
            if nums[i] > nums[i - 1]:
                decreasing = False
            i += 1
        
        return increasing or decreasing