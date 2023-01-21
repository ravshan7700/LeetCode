# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1:list, l2:list):
        ll1=str()
        ll2=str()

        for i in l1[::-1]:
            i=str(i)
            ll1+=i

        for i in l2[::-1]:
            i=str(i)
            ll2+=i

        ll1=int(ll1)
        ll2=int(ll2)
        ll1=str((ll1+ll2))
        ll2=[]
        for i in ll1[::-1]:
            ll2.append(i)
        
        return ll2


        


            
