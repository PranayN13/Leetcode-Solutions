class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        maximumArea = 0
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    maximumArea = max(maximumArea,self.dfs(grid,i,j))
        return maximumArea

    def dfs(self,grid,i,j):
        n = len(grid)
        m = len(grid[0])
        if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] != 1:
            return 0
        maximumArea = 1
        grid[i][j] = '#'
        maximumArea += self.dfs(grid,i+1,j)
        maximumArea +=  self.dfs(grid,i-1,j)
        maximumArea += self.dfs(grid,i,j+1)
        maximumArea += self.dfs(grid,i,j-1)
        
        return maximumArea
