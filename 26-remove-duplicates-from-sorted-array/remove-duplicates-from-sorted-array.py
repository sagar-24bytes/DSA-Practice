class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        idx=0
        n=len(nums)
        while i<n:
            while i<n-1 and nums[i]==nums[i+1]:
                i+=1
            
            nums[idx]=nums[i]
            idx+=1
            i+=1
        return idx

        


        
