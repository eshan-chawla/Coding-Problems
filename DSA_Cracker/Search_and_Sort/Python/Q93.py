#User function Template for python3

class Solution:
    def countSquares(self, N):
        k = (N)**0.5
        ans = math.floor(k)
        if(k==ans):
            ans-=1
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import math

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.countSquares(N))
# } Driver Code Ends