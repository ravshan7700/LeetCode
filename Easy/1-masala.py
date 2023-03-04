def malumot(lst: list):
    lst2=[[]]
    for i in lst:
        lst2.append([i])
        
    for j in range(len(lst)):
        if j == 1:
            lst2.append([lst[0],lst[j]])
            lst2.append([lst[j],lst[2]])
            lst2.append([[lst[0], lst[2]]])

    lst2.append(lst)
    return lst2

asdf=malumot(["a", "f", "z"])
print(asdf)

