class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        lst=[]
        for i in arr:
            if arr.count(i)==1:
                lst.append(i)
        if len(lst)>=k:
            return lst[k-1]
        return ""