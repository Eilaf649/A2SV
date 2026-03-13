a,b=map(int, input().split())
arr=list(map(int, input().split()))
left=0
sumi=0
maxi=0
for right in range(len(arr)):
    sumi+=arr[right]
    while sumi>b:
       sumi-=arr[left]
       left+=1
    maxi=max(maxi,right-left+1)
print(maxi)
       
        
        
    
