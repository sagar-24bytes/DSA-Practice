class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        arr=sorted(zip(position,speed),reverse=True)
        for pos,spd in arr:
            time=(target-pos)/float(spd)
            if not stack or stack[-1]<time:
                stack.append(time)
        return len(stack)
        