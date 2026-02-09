k,n,w=input().split()
k=int(k)
n=int(n)
w=int(w)
pay=0
for i in range(1,w+1):
    pay+=(i*k)
if pay-n <=0:
    print("0")
else:
    print(pay-n)
