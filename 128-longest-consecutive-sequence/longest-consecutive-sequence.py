class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        left=0

        max_len=0
        num_set=sorted(set(nums))
        for right in range(1,len(num_set)):
            if num_set[right]-1==num_set[right-1]:
                max_len=max(max_len,right-left+1)
                continue
            else:
                left=right
        return max_len if max_len!=0 else 1
        