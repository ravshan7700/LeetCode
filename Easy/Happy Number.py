class Solution:
    def isHappy(self, n: int) -> bool:
        while True:
            if n==1111111:
                return True
            n=str(n)
            sum=0
            for i in n:
                i=int(i)
                i=i*i
                sum+=i
            if sum==1:
                return True
            elif sum==len(n):
                return True
            elif sum>=2 and sum<=9 or sum==0:
                return False
            n=sum

