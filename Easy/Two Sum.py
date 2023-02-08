class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in nums:
            indexx=nums.index(i)
            if target - i in nums and nums.index(target-i)!=indexx:
                a=target-i
                a=nums.index(a)
                i=nums.index(i)
                lst=[a, i]
                return lst