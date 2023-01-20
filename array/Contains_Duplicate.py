class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        uzunlik=len(nums)
        nums=set(nums)
        nums=list(nums)
        uzunlik2=len(nums)
        
        if uzunlik==uzunlik2:
            return False
        return True