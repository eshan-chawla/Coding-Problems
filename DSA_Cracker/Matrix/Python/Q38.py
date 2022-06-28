class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=0
        j=0
        rows = len(matrix)
        columns = len(matrix[0])
        # print(f"rows : {rows}")
        # print(f"columns : {columns}")
        found = False
        while(i<rows):
            if(matrix[i][j]>target):
                i-=1
                break
            i+=1
        # print(i)
        if(i==rows):
            i-=1
            
        for j in range(columns):
            if(matrix[i][j]==target):
                found = True
                break
        return found
      