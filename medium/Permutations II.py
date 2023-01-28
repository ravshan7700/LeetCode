class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        son=1
        for i in range(1, (len(nums))+1):
            son*=i
        
        lst=[]
        print(son)
        for i in range(son):
            a=nums[0]
            nums.pop(0)
            nums.append(a)
            n=nums
            lst.append(n)
        nums=set(nums)
        nums=list(nums)
        return lst

