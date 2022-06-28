#User function Template for python3


def find(arr,n,x):
    found = False
    for i in range(n):
        if(arr[i]==x):
            if(found == True):
                a = min(a,i)
                b = max(b,i)
            else:
                found = True
                a = i
                b = i
        if(found == False):
            a=-1
            b=-1
    return a , b


#{ 
#  Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends