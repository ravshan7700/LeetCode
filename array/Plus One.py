class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        st=""
        for i in digits:
            i=str(i)
            st+=i
        st=int(st)
        st+=1
        st=str(st)
        st=[*st]
        st=list(map(int, st))
        return st
        

sp=Solution()
print(sp.plusOne([1,2,3]))