def ball(strr: str):
    summ=0
    for i in strr:
        i=i.lower()
        if i in "aeioulnstr":
            summ+=1
        elif i in "dg":
            summ+=2
        elif i in "bcmp":
            summ+=3
        elif i in "fhwvy":
            summ+=4
        elif i in "k":
            summ+=5
        elif i in "jx":
            summ+=8
        elif "qz":
            summ+=10
    
    return summ

asdf=ball("notebook")
print(asdf)
