import sys
x=int(input())
for _ in range(x):
    j=int(input())
    arr= list(map(int, input().split()))
    flag=True
    l=[]
    dis=[]
    arr.sort()
    for i in range(len(arr)):
        if i==0 and len(arr)>1:
            dis.append(abs(arr[i]-arr[i+1])) 
        elif i==len(arr)-1 and len(arr)>1:
            dis.append(abs(arr[i]-arr[i-1])) 
        elif len(arr)>1:
            dis1=abs(arr[i]-arr[i-1])
            dis2=abs(arr[i]-arr[i+1])
            dis.append(max(dis1,dis2))
        elif len(arr)==1:
            dis.append(1)
    for k in dis:
        if k>1:
            flag=False
    if flag==True:
        print("YES")
    else:
        print("NO")
    
        
