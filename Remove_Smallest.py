import sys
x=int(input())
for _ in range(x):
    j=int(input())
    arr= list(map(int, input().split()))
    flag=True
    for k in arr:
        for r in arr:
            if abs(k-r)>1:
                flag=False
    if flag==True:
        print("YES")
    else:
        print("NO")
    
        
