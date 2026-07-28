class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        ans=[]
        for hour in range(12):
            for minute in range(60):
                LED=bin(hour).count('1')+bin(minute).count('1')
                if LED == turnedOn:
                    ans.append("{}:{:02d}".format(hour,minute))
        return ans
        