class Solution:
    def canCross(self, stones: list[int]) -> bool:
        n=len(stones)
        target=stones[-1]
        if stones[1]!=1:
            return False

        stone_set=set(stones)
        seen=set()
        def func(idx,step):
            if idx==target:
                return True
            if (idx,step) in seen:
                return False
            seen.add((idx,step))
            for curr in (step-1,step,step+1):
                nxxt=curr+idx
                if curr>0 and nxxt in stone_set:
                    if func(nxxt,curr):
                        return True
            return False
        return func(1,1)

        