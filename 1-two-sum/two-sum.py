class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res={}
        for i in range(len(nums)):
            req=target-nums[i]
            if req in res:
                return [res[req],i]
            res[nums[i]]=i
        return [-1,-1]


        