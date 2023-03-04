class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sum1=0
        sum2=0
        for i in range(len(nums)):
            sum1=sum(nums[:i:])
            sum2=sum(nums[i+1::])

            if sum1==sum2:
                return i
        
            sum1=0
            sum2=0
        
        return -1

asdf=Solution()
print(asdf.pivotIndex([1,7,3,6,5,6]))