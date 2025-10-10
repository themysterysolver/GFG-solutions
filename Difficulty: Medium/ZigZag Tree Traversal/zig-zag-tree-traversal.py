'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def zigZagTraversal(self, root):
        # code here
        count = 0
        result = []
        q = deque([root])
        while q:
            l = len(q)
            res = []
            for _ in range(l):
                r = q.popleft()
                res.append(r.data)
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
            if count%2 == 1:
                result.extend(res[::-1])
            else:
                result.extend(res)
            count+=1
        return result
                    