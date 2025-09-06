'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        #code here
        count = 0
        s = dict()
        temp = head
        while temp:
            if temp in s:
                return count-s[temp] 
            s[temp] = count
            count+=1
            temp = temp.next
        return 0
        