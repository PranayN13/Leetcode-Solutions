class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(target):
            start,end = 0,len(nums)

            while(start<end):
                mid = start + (end - start) // 2
                if nums[mid] < target :
                    start =  mid + 1
                else:
                    end = mid
            return start
    
        start = search(target)
        end = search(target+1)-1
        
        if start <= end:
            return [start, end]
                
        return [-1, -1]
        