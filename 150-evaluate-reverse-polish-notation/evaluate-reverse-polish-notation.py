class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        stack=[]
        operators={'+','-','*','/'}
        def opr(x,y,op):
            if op=="+":
                return int(x+y)
            if op=="-":
                return int(x-y)
            if op=="*":
                return int(x*y)
            if op=="/":
                return int(x/y)
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                b=stack.pop()
                a=stack.pop()
                stack.append(opr(a,b,t))
        return stack[-1]

            
        