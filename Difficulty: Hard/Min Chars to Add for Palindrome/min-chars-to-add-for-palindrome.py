class Solution:
    def minChar(self, s):
        #Write your code here
        rev_s = s[::-1]
        
        # Form the combined string
        combined = s + '#' + rev_s
        
        # Compute the LPS array
        n = len(combined)
        lps = [0] * n
        for i in range(1, n):
            length = lps[i - 1]
            while length > 0 and combined[i] != combined[length]:
                length = lps[length - 1]
            if combined[i] == combined[length]:
                length += 1
            lps[i] = length
        
        # The LPS of the last character in combined gives the longest prefix of s
        # that matches a suffix of rev_s
        longest_palindromic_prefix = lps[-1]
        return len(s) - longest_palindromic_prefix

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input()
        obj = Solution()
        ans = obj.minChar(s)
        print(ans)
        print("~")

# } Driver Code Ends