#User function Template for python3

class Solution:
    def countSubarrays(self,nums, k):
        count=0
        hash={0:1}# 0 as a sum in prefix exist by default in nums. 
        prefixsum=0
        for num in nums:
            prefixsum+=num
            if prefixsum-k in hash:
                count+=hash[prefixsum-k]
            hash[prefixsum]=hash.get(prefixsum,0)+1
        return count



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.countSubarrays(arr, k)
        print(res)
        print("~")

# } Driver Code Ends