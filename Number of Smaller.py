i= map(int, input().split())
arr1=list(map(int, input().split()))
arr2=list(map(int, input().split()))
i=0
j=0
x=[]
for i in range(len(arr2)):
    while j<len(arr1):
        if arr2[i]>arr1[j]:
            j+=1
        else:
            break
    i+=1
    x.append(j)
print(*x)
