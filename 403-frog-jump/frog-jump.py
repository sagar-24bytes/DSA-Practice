class Solution:
    def canCross(self, stones: list[int]) -> bool:
        target=stones[-1]
        if stones[1]!=1:
            return False
        stone_set=set(stones)
        seen=set()

        def func(pos,k):
            if pos==target:
                return True
            if (pos,k) in seen:
                return False
            seen.add((pos,k))
            for x in (k-1,k,k+1):
                nxxt=pos+x
                if x>0 and nxxt in stone_set:
                    if func(nxxt,x):
                        return True
            return False
        return func(1,1)
        