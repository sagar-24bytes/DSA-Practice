class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=2:
            return len(nums)
        ins=2
        for i in range(2,len(nums)):
            if nums[i]!=nums[ins-2]:
                nums[ins]=nums[i]
                ins+=1
        return ins
        