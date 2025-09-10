class Solution:
    def largestSwap(self, s):
        #code here
        s = list(s)
        max_pos = [0]*len(s)
        max_idx = len(s)-1
        max_pos[-1] = max_idx
        
        for i in range(len(s)-2,-1,-1):
            if s[i]>s[max_idx]:
                max_pos[i] = i
                max_idx = i
            else:
                max_pos[i] = max_idx
        
        for i in range(len(s)):
            if s[max_pos[i]]>s[i]:
                s[max_pos[i]],s[i] = s[i],s[max_pos[i]]
                break
        return ''.join(s)
        