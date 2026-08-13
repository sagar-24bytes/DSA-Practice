class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ans=[0,0]
        for ch in moves:
            if ch=='U':
                ans[1]+=1
            elif ch=="D":
                ans[1]-=1
            elif ch=='L':
                ans[0]-=1
            elif ch=='R':
                ans[0]+=1
        return ans==[0,0]
        