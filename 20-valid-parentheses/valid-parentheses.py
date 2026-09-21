class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        symbols={'(':")", '{':'}', "[":']'}
        for ch in s:
            if ch in symbols:
                stack.append(ch)
            else:
                if not stack:
                    return False
                else:
                    if symbols[stack[-1]]==ch:
                        stack.pop()
                    else:
                        return False
        return True if not stack else False

        