#User function Template for python3

class Solution:
    def search(self, pat, txt):
        # code here
        # Function to preprocess the pattern and create the LPS array
        def computeLPSArray(pat):
            m = len(pat)
            lps = [0] * m
            length = 0  # Length of the previous longest prefix suffix
            i = 1

            while i < m:
                if pat[i] == pat[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        n = len(txt)
        m = len(pat)
        lps = computeLPSArray(pat)
        i = 0  # Index for txt
        j = 0  # Index for pat
        result = []

        while i < n:
            if pat[j] == txt[i]:
                i += 1
                j += 1

            if j == m:
                # Pattern found, store the starting index
                result.append(i - j + 1)  # 1-based index
                j = lps[j - 1]

            elif i < n and pat[j] != txt[i]:
                # Mismatch after j matches
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        for i in range(len(result)):
            result[i]-=1
        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans) == 0:
            print("[]", end="")
        for value in ans:
            print(value, end=' ')
        print()

# } Driver Code Ends