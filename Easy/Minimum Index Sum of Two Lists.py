class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        lst={}
        for i in list1:
            if i in list2:
                lst.update({i:(list1.index(i)+list2.index(i))})

        minn=min(lst.values())
        ls=[]
        for key, value in lst.items():
            if value==minn:
                ls.append(key)

        return ls

        
asdf=Solution()
print(asdf.findRestaurant(["ccc", 'qwert','asd', 'zx', 'asdf'],['qwert', 'wq','asdf', 'zx']))