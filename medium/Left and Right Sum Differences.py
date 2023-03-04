class Solution:
    def leftRigthDifference(self, nums: list[int]) -> list[int]:
        sum1=0
        sum2=0
        nums2=[]
        son=len(nums)
        for i in range(son):
            i=int(i)
            for j in nums[:i:]:
                sum1+=j
            for k in nums[(i+1)::]:
                sum2+=k

            if sum1>sum2:
                nums2.append(sum1-sum2)
            else:
                nums2.append(sum2-sum1)
            sum1=0
            sum2=0

        return nums2
    
asdf=Solution()
aaa=asdf.leftRigthDifference([10, 4, 8, 3])
print(aaa)



            
