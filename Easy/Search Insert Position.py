import PyQt5
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        for i in nums:
            if i>target:
                return nums.index(i)
            elif nums[len(nums)-1]<target:
                return nums.index()

sp=Solution()
print(sp.searchInsert([1,2, 3, 4, 5], 6))