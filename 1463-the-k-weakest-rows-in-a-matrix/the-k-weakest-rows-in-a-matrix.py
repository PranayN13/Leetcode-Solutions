class Solution:
    def kWeakestRows(self, mat, k):
        n = len(mat[0])
        for i in range(len(mat)):
            mat[i].append(i)
        
        mat.sort()
        
        ans = [mat[i][n] for i in range(k)]
        
        return ans
