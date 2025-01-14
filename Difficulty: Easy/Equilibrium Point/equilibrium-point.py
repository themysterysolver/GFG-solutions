# User function Template for python3

class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        prefix=[0]*len(arr)
        suffix=[0]*len(arr)
        prefix[0]=arr[0]
        suffix[-1]=arr[-1]
        for i in range(1,len(arr)):
            prefix[i]=prefix[i-1]+arr[i]
        for i in range(len(arr)-2,-1,-1):
            suffix[i]=suffix[i+1]+arr[i]
        #print(arr,prefix,suffix)
        for i in range(len(arr)):
            if prefix[i]==suffix[i]:
                return i
        return -1



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.findEquilibrium(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends