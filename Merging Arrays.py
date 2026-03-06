x,y= map(int, input().split())
arr1= list(map(int, input().split()))
arr2= list(map(int, input().split()))
i= 0
j=0
arr=[]
while i<len(arr1) and j<len(arr2):
    if arr1[i]<arr2[j]:
        arr.append(arr1[i])
        i+=1
    else:
        arr.append(arr2[j])
        j+=1
while j<len(arr2):
    arr.append(arr2[j])
    j+=1
while i<len(arr1):
    arr.append(arr1[i])
    i+=1
print(*arr)
