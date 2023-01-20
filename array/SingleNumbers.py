class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for i in nums:
            soni=nums.count(i)
            if soni>=2:
                pass
            else:
                return i