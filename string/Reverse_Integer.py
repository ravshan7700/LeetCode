class Solution:
    def reverse(self, x: int) -> int:
        y=str()
        x=str(x)
        if x[0]=="-":
            for i in x[1:]:
                y+=i
        for i in y[::-1]:
            x+=i
        return x      