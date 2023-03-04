class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index=len(nums)-1
        son=0
        while nums:
            while nums:
                if nums[son]+nums[index]==target:
                    return [son, index]
                if index==1:
                    break
                index-=1
            son+=1
            index=len(nums)-1
        return []
asdf=Solution()
print(asdf.twoSum([3,3], 6))