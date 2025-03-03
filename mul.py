import math
text="20+30*2-1"
text=text.split("+")
def mul(text):
    d = text.index("*")
    #e=int(text[0:d]) * int(text[d + 1:len(text)])
    print(text.count("*"))
    #print(str(e))
    print(text)
    if text.count("*")==1 | text.count("x")==1:
        e = int(text[0:d]) * int(text[d + 1:len(text)])
        return e
    else:
        text1=text.split("*")
        print(len(text1))
        print(text1)

print(mul(text))