class Solution:


    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        numss=[]
        for i in nums:
            count=0
            for j in nums:
                if i>j:
                    count+=1
            numss.append(count)
        return numss