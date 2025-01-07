#User function Template for python3


class Solution:
    def countPairs(self,arr, target):
        res = 0
        n = len(arr)
        left = 0
        right = n - 1
    
        while left < right:
    
            # If sum is greater
            if arr[left] + arr[right] < target:
                left += 1
    
            # If sum is lesser
            elif arr[left] + arr[right] > target:
                right -= 1
    
            # If sum is equal
            else:
                cnt1 = 0
                cnt2 = 0
                ele1 = arr[left]
                ele2 = arr[right]
    
                # Count frequency of first element of the pair
                while left <= right and arr[left] == ele1:
                    left += 1
                    cnt1 += 1
    
                # Count frequency of second element of the pair
                while left <= right and arr[right] == ele2:
                    right -= 1
                    cnt2 += 1
    
                # If both the elements are same, then count of
                # pairs = the number of ways to choose 2
                # elements among cnt1 elements
                if ele1 == ele2:
                    res += (cnt1 * (cnt1 - 1)) // 2
    
                # If the elements are different, then count of
                # pairs = product of the count of both elements
                else:
                    res += (cnt1 * cnt2)
    
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0].strip())
    index = 1

    for _ in range(t):
        arr = list(map(int, data[index].strip().split()))
        index += 1
        target = int(data[index].strip())
        index += 1

        res = Solution().countPairs(arr, target)
        print(res)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends