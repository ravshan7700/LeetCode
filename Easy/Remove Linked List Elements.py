# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: list, val: int):
        for i in head:
            if i==val:
                head.remove(i)
        return head

sp=Solution()
print(sp.removeElements([1,2,6,3,4,5,6], 6))