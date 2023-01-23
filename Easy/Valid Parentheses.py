class Solution:
    def isValid(self, s: str) -> bool:
        son=0
        bul=False
        while son < len(s):
            if s[son]=="[" and s[son+1]=="]":
                pass
            else:
                bul=True
            if s[son]=="{" and s[son+1]=="}":
                pass
            else:
                bul=True
            if s[son]=="(" and s[son+1]==")":
                pass
            else:
                bul=True

            if len(s)==2 and bul==True:
                return True
        return True