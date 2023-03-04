class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        count=0
        son=len(nums)

        while son:
            if nums[son-1]==val:
                nums.pop(son-1)
                count+=1
            son-=1

asdf=Solution()
nimadur=asdf.removeElement([0,1,2,2,3,0,4,2], 2)
print(nimadur) 
                