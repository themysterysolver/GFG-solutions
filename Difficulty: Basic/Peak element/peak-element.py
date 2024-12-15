
class Solution:   
    def peakElement(self,arr):
        # Code here
        def peakFind(arr):
            n = len(arr)
        
            # If there is only one element, then it's a peak
            if n == 1:
                return 0
        
            # Check if the first element is a peak
            if arr[0] > arr[1]:
                return 0
        
            # Check if the last element is a peak
            if arr[n - 1] > arr[n - 2]:
                return n - 1
        
            # Search Space for binary Search
            lo, hi = 1, n - 2
        
            while lo <= hi:
                mid = lo + (hi - lo) // 2
        
                # If the element at mid is a  
                # peak element return mid
                if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                    return mid
        
                # If next neighbor is greater, then peak
                # element will exist in the right subarray
                if arr[mid] < arr[mid + 1]:
                    lo = mid + 1
        
                # Otherwise, it will exist in left subarray
                else:
                    hi = mid - 1
        return peakFind(arr)
        


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        arr = list(map(int, input().split()))
        # Create a Solution object and calculate the result

        index = Solution().peakElement(arr)
        n = len(arr)
        flag = False
        if index < 0 or index >= n:
            flag = False
        else:
            if index == 0 and n == 1:
                flag = True
            elif index == 0 and arr[index] > arr[index + 1]:
                flag = True
            elif index == n - 1 and arr[index] > arr[index - 1]:
                flag = True
            elif index > 0 and index < n - 1 and arr[
                    index - 1] < arr[index] and arr[index] > arr[index + 1]:
                flag = True
            else:
                flag = False

        if flag:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends