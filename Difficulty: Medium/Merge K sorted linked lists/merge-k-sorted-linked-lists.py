'''
class Node:
    def _init_(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    def mergeKLists(self, arr):
        # code here
        def mergeIt(l1,l2):
            dummy = Node(0)
            temp = dummy
            while l1 and l2:
                if l1.data<l2.data:
                    temp.next = l1
                    l1 = l1.next
                else:
                    temp.next = l2
                    l2 = l2.next
                temp = temp.next
            temp.next = l1 or l2
            return dummy.next
        
        def merge(arr):
            if len(arr) == 0:
                return None
            if len(arr) == 1:
                return arr[0]
            mid = len(arr)//2
            left = merge(arr[:mid])
            right = merge(arr[mid:])
            return mergeIt(left,right)
        return merge(arr)
                
            
                    
        