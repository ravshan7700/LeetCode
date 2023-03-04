class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        aa=nums
        lst=[]
        lst.extend(nums)
        while True:
            a=nums
            print(a)
            nums.remove(a)
            print(nums)
            nums.append(a)
            print(nums)
            if nums!=aa:
                lst.extend(nums)
            else:
                return lst

asdf=Solution()
print(asdf.permute([[1,2,3]]))
            

