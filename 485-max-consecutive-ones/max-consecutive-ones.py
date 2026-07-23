class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len=0
        length=0
        for n in nums:
            if n==1:
                length+=1
            else:
                length=0
                continue
            max_len=max(max_len,length)
        return max_len
        