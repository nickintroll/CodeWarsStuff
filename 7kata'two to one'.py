a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"

def longest(a1, a2):
    a = sorted(list({i for i in a1 + a2}))
    return ''.join(a)




print(longest(a, b))