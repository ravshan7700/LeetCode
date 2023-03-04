class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            x=nums.index(target)
            return x
        
        nums=sorted(nums)
        print(nums)
        
        for i in nums:
            if i > target:
                return nums.index(i)
        return len(nums)
        

asdf=Solution()
# asdf.searchInsert([1, 2, 3, 4, 5],5)
print(asdf.searchInsert([4,3,5,6],7))