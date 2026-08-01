from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        left=0
        ans=[]
        q=deque()
        for right in range(len(nums)):
            while q and nums[q[-1]]<nums[right]:
                q.pop()
            q.append(right)
            while q and q[0]<left:
                q.popleft()
            if right-left+1==k:
                ans.append(nums[q[0]])
                left+=1
        return ans 