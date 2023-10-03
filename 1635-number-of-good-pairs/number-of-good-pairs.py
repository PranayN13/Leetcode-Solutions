class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashMap = {}
        res = 0
        for num in nums:            
            if num in hashMap:
                res += hashMap[num]
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        return res