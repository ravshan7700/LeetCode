
class Solution:
    def mergeTwoLists(self, list1:list, list2:list):
            for i in list2:
                list1.append(i)
                
            n = len(list1)
            swapped = False
            
            for i in range(n-1):
                for j in range(0, n-i-1):
                    if list1[j] > list1[j + 1]:
                        swapped = True
                        list1[j], list1[j + 1] = list1[j + 1], list1[j]
                
                if not swapped:
                    break
            
            return list1
