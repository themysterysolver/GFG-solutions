class Solution:
    def reverseQueue(self, q):
        # code here
        stack = []
        l = len(q)
        for _ in range(l):
            stack.append(q.popleft())
        
        while stack:
            q.append(stack.pop())
        return q
        