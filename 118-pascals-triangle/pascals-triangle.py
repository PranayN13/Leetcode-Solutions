class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []          
        for row in range(numRows): 
            new_row = [1] * (row + 1)  
            
            for col in range(1, row):  
                new_row[col] = res[row - 1][col - 1] + res[row - 1][col]
            res.append(new_row) 
        
        return res 