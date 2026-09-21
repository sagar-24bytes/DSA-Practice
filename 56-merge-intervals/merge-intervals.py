class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        if len(intervals)<=1:
            return intervals
        ans=[]
        for inter in intervals:
            if ans and ans[-1][1]>=inter[0]:
                ans[-1][1]=max(ans[-1][1],inter[1])
            else:
                ans.append(inter)
        return ans
        