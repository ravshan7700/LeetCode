class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        lst=[]
        for i in range(1,n+1):
            if i%3==0 and i%5!=0:
                lst.append("Fzz")
            elif i%5==0 and i%3!=0:
                lst.append("Buzz")
            elif i%5==0 and i%3==0:
                lst.append("FizzBuzz")
            else:
                lst.append(i)
        return lst