#User function Template for python3

class Solution:
    def rotate(self, arr):
        el = arr.pop()
        arr.insert(0,el)
        return arr
