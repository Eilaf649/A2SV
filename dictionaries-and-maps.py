from sys import stdin 
res=dict()
num= int(input())
for _ in range (num):
    name, phone= input().split()
    res[name]=phone
lines = stdin.read().splitlines()
for i in range(len(lines)):
    if lines[i] in res.keys():
        print(lines[i]+"="+res[lines[i]])
    else:
        print("Not found")
