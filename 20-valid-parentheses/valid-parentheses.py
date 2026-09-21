class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        symbols={'(':")", '{':'}', "[":']'}
        for ch in s:
            if ch in symbols:
                stack.append(ch)
            else:
                if not stack or symbols[stack[-1]]!=ch:
                    return False
                stack.pop()
                
        return True if not stack else False

        