x=int(input())
y=list(map(int, input().split()))
e=0
o=0
for j in y:
    if j%2==0:
        e+=1
    else:
        o+=1
if o>=1 and e>=1:
    y.sort()
print(*y)
