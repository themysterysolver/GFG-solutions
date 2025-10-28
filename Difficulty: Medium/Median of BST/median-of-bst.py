'''
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMedian(self, root):
        # code here
        inord = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            inord.append(root.data)
            inorder(root.right)
        inorder(root)
        #print(inord)
        if len(inord)%2 == 0:
            #print(inord[len(inord)//2],len(inord)//2)
            return inord[len(inord)//2-1]
        else:
            return inord[(len(inord)+1)//2-1]