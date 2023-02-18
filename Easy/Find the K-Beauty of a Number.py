class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        # num=240 k=2
        son=0
        num2=str()
        while True:
            num=str(num)
            num2=num[son:(son+k)]
            print(num2)
            num=int(num)
            num2=int(num2)

            if num%num2==0:
                pass
            else:
                return False
            son+=1
            num=str(num)
            if son==len(num):
                return True

sp=Solution()
print(sp.divisorSubstrings(240,2))

