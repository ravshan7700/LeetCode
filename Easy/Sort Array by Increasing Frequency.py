class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        nums1=[]
        nums2=[]
        for i in range(len(nums)):
            for j in nums:
                print(j)

                if nums.count(j) == i+1:
                    for k in range(i+1):
                        nums1.append(j)
                        nums.remove(j)
                    
            
                nums1.sort(reverse=True)
                for m in nums1:
                    nums2.append(m)
                
                nums1.clear()
        
        return nums2

            




            
asdf=Solution()
print(asdf.frequencySort([8,-8,2,-8,-5,-3]))