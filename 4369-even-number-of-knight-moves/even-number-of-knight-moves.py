class Solution(object):
    def canReach(self, start, target):
        """
        :type start: List[int]
        :type target: List[int]
        :rtype: bool
        """
        a=sum(start)%2
        b=sum(target)%2
        return a==b
        