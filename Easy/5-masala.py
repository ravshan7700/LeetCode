def IP(n: int):
    lst=[]
    for i in range(n):
        son=input(f"{i+1} - ip ni kiriting: ")
        lst.append(son)
    son=3
    sum=0
    lst2=[]
    for i in lst:
        i=str(i)
        i=i.split(".")
        for j in i:
            j=int(j)
            sum+=j*pow(256, son)
            son-=1
        lst2.append(sum)
        son=3
    
    lst2.sort()

    for i in lst:
        i=str(i)
        i=i.split(".")
        for j in i:
            j=int(j)
            sum+=j*pow(256, son)
            son-=1
        
        son=3


        



    

