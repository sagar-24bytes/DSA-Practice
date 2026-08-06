import math
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        arr=[int(x) for x in list(str(n))]
        for i in range(n,101):
            arr=[int(x) for x in list(str(i))]
            a=math.prod(arr)
            if a%t==0:
                return i
        return -1


         
        