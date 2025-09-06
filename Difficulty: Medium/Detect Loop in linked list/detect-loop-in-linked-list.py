'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def detectLoop(self, head):
        # code here
        slow,fast = head,head
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
        
