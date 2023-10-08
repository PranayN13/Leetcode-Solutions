class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n , m = len(nums1) , len(nums2)
        memory = [[float('-inf')] * m for _ in range(n)]

        def dp(i, j):
            if i == n or j ==m :
                return float('-inf')
            
            if memory[i][j] != float('-inf'):
                return memory[i][j]

            memory[i][j] = max(
                nums1[i] * nums2[j] + max(dp(i + 1, j + 1),0),dp(i + 1,j), dp(i,j + 1),
            )

            return memory[i][j]
        return dp(0,0)