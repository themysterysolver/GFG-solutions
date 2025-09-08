'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def mergeSort(self, head):
        # code here
        def middle(node):
            slow,fast = node,node
            while fast.next and fast.next.next:
                slow =slow.next
                fast = fast.next.next
            return slow
        
        def merges(node):
            if node is None or node.next is None:
                return node
            prev = middle(node)
            mid = prev.next
            prev.next = None
            return merge(merges(node),merges(mid))
        
        def merge(l1,l2):
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
        
        return merges(head)
                    
        