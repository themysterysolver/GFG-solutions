class Solution:
    def minParentheses(self, s):
        # code here
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(c)
        #print(stack)
        return len(stack)
        
        