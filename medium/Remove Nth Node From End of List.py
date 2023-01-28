# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head:list, n):
        for i in range(len(head)-1):
            if i==n:
                head.pop(i)
        return head



sp=Solution()
print(sp.removeNthFromEnd([1, 2, 3, 4, 5, 6, 6], 4))
