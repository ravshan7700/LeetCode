class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss=str()
        for i in s:
            i=str(i)
            if i.isalpha():
                i=i.lower()
                ss+=i
            elif i.isdigit():
                ss+=i
        if ss==ss[::-1]:
            return True
        return False