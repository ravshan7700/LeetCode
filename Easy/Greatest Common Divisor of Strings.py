class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2==str2+str1:
            if len(str1)>len(str2):
                return str2
            else:
                return str1
        else:
            return ""