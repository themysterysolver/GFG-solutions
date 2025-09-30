class Solution:
    def binstr(self, n):
        # code here
        result = []
        def go(b,c):
            if c<0:
                return
            #print(b,c)
            if c == 0:
                result.append(b)
                return
            for bc in ['0','1']:
                go(b+bc,c-1)
        go("",n)
        return result
            