#User function Template for python3

class Solution:
    def postToInfix(self, postfix):
        # Code here
        operand = []
        for c in postfix:
            if c not in {'+','-','*','/'}:
                operand.append(c)
            else:
                e1 = operand.pop()
                e2 = operand.pop()
                if c == '+':
                    operand.append(f"({e2}+{e1})")
                if c == '-':
                    operand.append(f"({e2}-{e1})")
                if c == '*':
                    operand.append(f"({e2}*{e1})")
                if c == '/':
                    operand.append(f"({e2}/{e1})")
                if c == '^':
                    operand.append(f"({e2}^{e1})")
        return operand[-1]
                