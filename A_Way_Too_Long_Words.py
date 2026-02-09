x=int(input())
for _ in range(x):
    word=input()
    if len(word)>10:
        l=str(len(word)-2)
        print(word[0]+l+word[len(word)-1])
    else:
        print(word)
