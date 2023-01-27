class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        son=0
        lst=[]
        while len(nums)>son:
            lst.append(nums[nums[son]])
            son+=1
        return lst

sp=Solution()
print(sp.buildArray([2, 3, 1, 4, 5, 0]))