class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        harf=s[0]
        chack=False
        lst=[harf]
        sss=s
        for i in s[1::]:
            if i!=harf:
                lst.append(i)
            else:
                break
        son=len(lst)
        if len(s)/son!=0:
            return False
        
        sss="".join(lst)
        print(sss)
        s.split(sss)
        print(s)

            
s=Solution()
s.repeatedSubstringPattern("asdakhgfcoytdsdasdd")