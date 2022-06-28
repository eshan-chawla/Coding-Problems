#User function Template for python3

class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        
        # We will use R , C to know about where to traverse
        i=0
        j=-1
        ans = []
        left = 0
        right = c
        top = 0
        down = r
        length = r*c
        
        while(left<right and top<down):
            
            # Move right
            while(j<right-1):
                j+=1
                ans.append(matrix[i][j])
                
            top+=1
            
            #move Down
            while(i<down-1):
                i+=1
                ans.append(matrix[i][j])
                
            right -=1
            
            if(length == len(ans)):
                break
            
            #move left
            while(j>left):
                j-=1
                ans.append(matrix[i][j])
                
            down -=1
            
            
            #move up
            while(i>top):
                i-=1
                ans.append(matrix[i][j])
            
            left+=1
            
            if(length == len(ans)):
                break

        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends