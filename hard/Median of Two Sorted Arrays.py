class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        a=sorted(nums1)
        count=len(a)

        if count%2==0:
            return ((a[count//2-1] + a[(count//2)]) / 2)
        else:
            return a[(count//2)]
