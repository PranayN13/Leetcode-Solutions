class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minSoFar = prices[0]
        maxPro = 0

        for i in range(1,n):
            minSoFar = min(minSoFar,prices[i])
            maxPro = max(maxPro,prices[i] - minSoFar)
        return maxPro