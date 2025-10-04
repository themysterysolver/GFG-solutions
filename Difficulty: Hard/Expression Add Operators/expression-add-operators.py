#GOATED APPROACH
#https://www.geeksforgeeks.org/dsa/print-all-possible-expressions-that-evaluate-to-a-target/
class Solution:
    def findExpr(self, s, target):
        # code here
        res = []
        def backtrack(idx,expr,curr,prev):
            if idx == len(s):
                if curr == target:
                    res.append(expr)
                return
            for i in range(idx,len(s)):
                if idx!=i and s[idx]=='0':
                    break
                part = s[idx:i+1]
                digit = int(part)
                if idx==0:
                    backtrack(i+1,expr+part,digit,digit)
                else:
                    backtrack(i+1,expr+"+"+part,curr+digit,digit)
                    backtrack(i+1,expr+"-"+part,curr-digit,-digit)
                    backtrack(i+1,expr+"*"+part,curr-prev+prev*digit,prev*digit)
        backtrack(0,"",0,0)
        return res
        
        