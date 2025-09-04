"""
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""

class Solution:
    def reverseKGroup(self, head, k):
        # Code here
        temp = head
        for _ in range(k):
            temp = temp.next
            if not temp:
                break
        if temp:
            temp = head
            prev = None
            for _ in range(k):
                nexti = temp.next
                temp.next = prev
                prev = temp
                temp = nexti
            head.next = self.reverseKGroup(temp,k)
            return prev
        else:
            prev = None
            temp = head
            while temp:
                nexti = temp.next
                temp.next = prev
                prev = temp
                temp = nexti
            return prev
            
        return self.reverseKGroup(head,k)