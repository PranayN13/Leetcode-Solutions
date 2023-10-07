class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if m < k:
            return 0
        
        # Initialize a 2D array for dynamic programming
        # dp[i][j] represents the number of ways to construct an array of length i+1 with maximum element j+1
        dp = [[1] * m] + [[0] * m for _ in range(k - 1)]
        
        mod = 10 ** 9 + 7
        
        # Iterate through the elements
        for _ in range(n - 1):
            for i in range(k - 1, -1, -1):
                cur = 0
                for j in range(m):
                    # Update dp[i][j] using the given recurrence relation
                    dp[i][j] = (dp[i][j] * (j + 1) + cur) % mod
                    if i:
                        cur = (cur + dp[i - 1][j]) % mod
        
        # Calculate the total number of arrays for length n with at most m as the maximum element
        total_arrays = sum(dp[-1]) % mod
        return total_arrays
