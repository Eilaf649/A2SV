from collections import Counter
n,k=map(int,input().split())
y=list(map(int, input().split()))
y.sort()
c=Counter(y)
a=0
arr=[]
if k==0 and y[0]>1:
    print(1)
    exit()
    
for val in c.values():
    a+=val
    arr.append(a)
#print(arr)
if k not in arr:
    print(-1)
else:
    st=list(set(y))
    print(y[k-1])
