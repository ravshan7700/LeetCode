def dublikat(st: str):
    ls=[]
    ls2=[]
    for i in st:
        if i not in ls:
            ls.append(i)
            ls2.append(i)
        else:
            ls.append(i)
            ls2.append(f"{i}_{ls.count(i)-1}")
            
    
    return ls2

asdf=dublikat("aaabcaadcdd")
print(asdf)