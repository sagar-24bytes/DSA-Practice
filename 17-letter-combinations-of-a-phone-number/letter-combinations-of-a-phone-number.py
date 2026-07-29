class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        ans=[]
        def func(idx,path):
            if idx==len(digits):
                ans.append(path)
                return
            code=phone[digits[idx]]
            for ch in code:
                func(idx+1,path+ch)
        func(0,"")
        return ans 
            

        