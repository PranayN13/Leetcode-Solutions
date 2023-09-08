class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            return []
        res = []          
        for row in range(rowIndex+1): 
            new_row = [1] * (row + 1)  
            
            for col in range(1, row):  
                new_row[col] = res[row - 1][col - 1] + res[row - 1][col]
            res.append(new_row) 
        
        return res[rowIndex]
        