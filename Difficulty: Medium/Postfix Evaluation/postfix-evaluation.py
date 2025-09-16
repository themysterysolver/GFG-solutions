import re
class Solution:
    def evaluatePostfix(self, arr):

        operand = []
        
        for el in arr:
            # check if it's a number (possibly signed)
            if re.match(r"^[+-]?\d+$", el):
                operand.append(int(el))
            else:
                e1 = operand.pop()
                e2 = operand.pop()
                if el == "+":
                    operand.append(e2 + e1)
                elif el == "-":
                    operand.append(e2 - e1)
                elif el == "*":
                    operand.append(e2 * e1)
                elif el == "/":
                    operand.append(e2 // e1)
                elif el == "^":
                    operand.append(e2 ** e1)
        
        return operand[-1]
        