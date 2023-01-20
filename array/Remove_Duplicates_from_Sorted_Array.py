class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums=set(nums)
        nums=list(nums)
        nums=sorted(nums)
        a=len(nums)
        return a