#User function Template for python3

class Solution:
    def middle(self,A,B,C):
        if(A>B):
            # ik A>B
            if(B>C):
                #ik A>B and B>C => B is middle element
                ans = B
            elif(C>A):
                #ik A>B and C>A  => A is middle element 
                ans = A
            else:
                #ik if ans is not A,B it is C
                ans = C
        # ik that B>A
        elif(A>C):
            #ik B>A and A>C
            ans = A
        
        elif(B>C):
            #ik B>A and C>A and B>C => C is middle element
            ans = C
            
        else :
            #ik B>A , C>A , C>B => B is middle element
            ans = B
                
        return ans



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        A,B,C=map(int,input().strip().split())
        ob=Solution()
        print(ob.middle(A,B,C))
# } Driver Code Ends