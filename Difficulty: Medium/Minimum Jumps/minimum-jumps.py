class Solution:
	def minJumps(self, nums):
	    jump,bound,farthest = 0,0,0
	    for i in range(len(nums)-1):
	        if i>farthest:
	            return -1
	        
	        farthest = max(farthest,i+nums[i])
	        if i == bound:
	            bound = farthest
	            jump+=1
            if bound>=len(nums)-1:
                return jump
	    return -1
	   
	    
	    