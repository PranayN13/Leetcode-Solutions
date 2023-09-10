class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]
        ans = 1
        
        for i in range(1,len(nums)):
            currentVal = 1 
            for j in range(0,i):
                if nums[j]<nums[i]:
                    currentVal = max(currentVal, dp[j]+1)
            dp.append(currentVal)
            ans = max(ans,dp[i])
        return ans