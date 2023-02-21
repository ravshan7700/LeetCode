class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        count=0
        for i in s:
            for j in g:
                if i>=j:
                    count+=1
                    g.remove(j)
                    break
        return count
s=Solution()
print(s.findContentChildren([1, 2, 3], [1, 2]))