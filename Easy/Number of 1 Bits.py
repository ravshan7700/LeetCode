class Solution:
    def hammingWeight(self, n: int) -> int:
        n=str(n)
        return n.count("1")

sp=Solution()
print(sp.hammingWeight("00000000000000000000000000001011"))