n,t=map(int, input().split())
arr=list(map(int, input().split()))
sumi=0
maxi=0
left=0
for right in range(len(arr)):
    sumi+=arr[right]
    while sumi>t and left<len(arr):
        sumi-=arr[left]
        left+=1  
    maxi=max(maxi, right-left+1)
print(maxi)
