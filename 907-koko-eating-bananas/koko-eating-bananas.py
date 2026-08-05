class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        while left<=right:
            mid=(left+right)//2
            hours=0
            for p in piles:
                if p%mid==0:
                    hours+=(p//mid)
                else:
                    hours+=(p//mid)+1
            if hours<=h:
                right=mid-1
            else:
                left=mid+1
        return left
        