'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def postOrder(self, root):
        # code here
        res = []
        def pos(root):
            if not root:
                return 
            pos(root.left)
            pos(root.right)
            res.append(root.data)
        pos(root)
        return res
            
        
        