def soztop(lst: list, chars: str):
    chars2=[]
    for i in chars:
        chars2.append(i)

    count=0
    summa=0

    for i in lst:

        for j in i:

            if j in chars2:
                chars2.remove(j)
                count+=1
            else:
                break
        if len(i)==count:
            summa+=len(i)
        count=0
    return summa

asdf=soztop(['qwer', 'asd', 'zxcv'], "qwerasdfzxcvb")
print(asdf)