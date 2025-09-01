#User function Template for python3

class Solution:
    def increment(self, arr, N):
        # code here 
        num = arr[::-1]
        carry = 1
        for i in range(len(num)):
            carry += num[i]
            num[i] = carry%10
            carry = carry//10
        if carry!=0:
            num.append(carry)
        #print(num)
        arr = num[::-1]
        return arr