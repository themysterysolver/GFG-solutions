'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def swapKth(self, head, k):
        
        temp = head
        slow = head
        for _ in range(k-1):
            if temp:
                temp = temp.next
            else:
                return head
        leftSwap = temp
        
        fast = temp
        slow = head
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        #print(slow.val)
        slow.data,leftSwap.data = leftSwap.data,slow.data
        return head
        
        
        
                
        
