class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        ans=[]
        n=len(intervals)
        if n<=1:
            return intervals
        for interval in intervals:
            if ans and ans[-1][1]>=interval[0]:
                ans[-1][1]=max(interval[1],ans[-1][1])
            else:
                ans.append(interval)
        return ans        