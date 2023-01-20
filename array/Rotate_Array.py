class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            a=nums[len(nums)-1]
            nums.pop(len(nums)-1)
            nums.insert(0,a)
            
        return nums