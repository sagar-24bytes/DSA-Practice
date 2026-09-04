class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited=set()
        def func(idx):
            if idx<0 or idx>=len(arr) or idx in visited:
                return False
            visited.add(idx)
            if arr[idx]==0:
                return True
            return func(idx+arr[idx]) or func(idx-arr[idx])
        return func(start)
            

 
        