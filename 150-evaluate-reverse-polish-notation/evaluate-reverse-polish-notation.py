class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        def opr(x,op,y):
            if op=="+":
                return x+y
            elif op=="-":
                return x-y
            elif op=="*":
                return x*y
            else:
                return int(x/y)
        for ch in tokens:
            if ch not in "+-*/":
                stack.append(int(ch))
            else:
                if stack:
                    b=stack.pop()
                    a=stack.pop()
                    stack.append(opr(a,ch,b))
        
        return stack[-1]
        
        