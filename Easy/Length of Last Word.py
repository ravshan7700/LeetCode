class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        s=s.split()
        s=s[-1]
        return len(s)
    
asdf=Solution()
print(asdf.lengthOfLastWord("nimadur va kimdur   "))