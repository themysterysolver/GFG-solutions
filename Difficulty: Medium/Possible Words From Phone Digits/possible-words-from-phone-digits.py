class Solution:
    def possibleWords(self, arr):
        # code here
        result = []
        hash = {0:"",1:"",2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        def backtrack(idx,path):
            if idx == len(arr):
                result.append(path)
                return
            else:
                name = hash[arr[idx]]
                if arr[idx] in [0,1]:
                    backtrack(idx+1,path)
                for i in range(len(name)):
                    backtrack(idx+1,path+name[i])
        backtrack(0,"")
        return result
                
