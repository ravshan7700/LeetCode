class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        count=0
        lst=[]
        sum=0
        for i in nums:
            for j in range(count):
                sum+=nums[j]
            lst.append(sum)
            sum=0
            count+=1
        return lst