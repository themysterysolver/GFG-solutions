class Solution:
    def decodedString(self, s):
        # code here
        stack = []
        numStack = []
        num = 0
        for c in s:
            if c.isdigit():
                num*=10
                num+=int(c)
            elif c == '[':
                stack.append(c)
                numStack.append(num)
                num = 0
            elif c!=']':
                stack.append(c)
            else:
                string = ''
                while stack and stack[-1]!='[':
                    el = stack.pop()
                    string = el+string
                stack.pop()
                stack.append(string*numStack.pop())
                
        return ''.join(stack)