'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''

class Solution:
    def getMiddle(self, head):
        # code here
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
        
