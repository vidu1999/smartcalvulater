text = "(078(1*8*2)103)"

a = text.index("(")
b = text.index(")")
c = len(text)
def calcu(text,a,b,c):
    if a>b:
        if '(' in text[a+1:b]:
            a=text[a+1:b].index("(")
            text=text[a+1:b]

        if '*' in text[a+1:b] | 'x' in text[a+1:b]:
                mul(text)

calcu(text, a, b, c, )
def mul(text):
    d = text.index("*")
    e=text.index[d - 1] * text.index[d + 1]
    if text.count("*")==1 | text.count("x")==1:
        return e
    elif text[d+1:len(text)].count("*")>1 | text[d+1:len(text)].count("x")>1:
        text=text[d+1:len(text)]
        return e*mul(text)


print(text)
print(a)
print(b)
print(c)
print(calcu(text, a, b, c))

print(a)
