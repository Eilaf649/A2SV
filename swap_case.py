def swap_case(s):
    res=""
    for c in s:
        if c.islower():
            c=c.upper()
        elif c.isupper():
            c=c.lower()
        res+=c
    return res
if __name__ == '__main__':
