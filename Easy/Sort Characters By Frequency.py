class Solution:
    def frequencySort(self, s: str) -> str:
        lst=[]
        ls=[]
        lst2={}
        for i in s:
            ls.append(i)
            if s.count(i)>1:
                lst2.update({i:s.count(i)})
            else:
                lst.append(i)
        
        lst.sort()
        print(lst2)

        lst4=[]
        lst5=[]
        for key, value in lst2.items():
            lst4.append(key)
            lst5.append(value)
        

            

        for i in lst4:
            for j in lst5:
                if i*j==ls.count(i):
                    pass

        # lst3=[]
        # for i in lst2:
        #     harf=str(i[0])
        #     son=int(i[1])
        #     lst3.append(harf*son)
        
        # lst3.extend(lst)
        # lst="".join(lst3)

        return lst



s=Solution()
print(s.frequencySort("cccaaa"))