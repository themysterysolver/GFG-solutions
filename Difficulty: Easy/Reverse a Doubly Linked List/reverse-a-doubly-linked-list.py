"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        # code here
        prev = None
        temp = head
        
        if head is None or head.next is None:
            return head
            
        while temp:
            
            prev = temp.prev
            temp.prev = temp.next
            temp.next = prev
            temp = temp.prev
            
        return prev.prev
            
        
        