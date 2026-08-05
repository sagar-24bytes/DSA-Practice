class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        s=sum(candies)
        if s<k:
            return 0
        left=1
        right=max(candies)
        while left<=right:
            mid=(left+right)//2
            children=0
            for c in candies:
                children+=(c//mid)
            if children>=k:   # valid
                left=mid+1
            else:
                right=mid-1
        return right   # here right is last valid and left is last invalid after while loop ends 
                 
        