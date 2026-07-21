class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ins=0
        i=0
        while i<len(nums):
            x=1

            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
                x+=1
            if x>=2:
                nums[ins]=nums[i]
                ins+=1
                nums[ins]=nums[i]
                # ins+=1
            else:
                nums[ins]=nums[i]
            ins+=1
            i+=1
        return ins