def mutate_string(string, position, character):
    string=list(string)
    string[position]=character
    x=""
    for s in string:
        x+=s
    return x
if __name__ == '__main__':
