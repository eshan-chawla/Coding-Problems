
class Solution:
    def merge(self, arr1, arr2, n, m):
        for i in range(m):
            arr1.append(arr2[i])
        arr1.sort()
        for i in range(m):
            arr2.pop()
        return arr1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":         
    tc=int(input())
    while tc > 0:
        n, m=map(int, (input().strip().split()))
        arr1=list(map(int , input().strip().split()))
        arr2=list(map(int , input().strip().split()))
        ob = Solution()
        ans=ob.merge(arr1, arr2, n, m)
        for x in arr1:
            print(x, end=" ")
        for x in arr2:
            print(x, end=" ")
        print()
        tc=tc-1
# } Driver Code Ends