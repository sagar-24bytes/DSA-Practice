class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        count=0
        intervals=[]
        for i in range(n+1):
            intervals.append([i-ranges[i], i+ranges[i]])
        intervals.sort()
        covered=0
        idx=0
        farthest=0
        while covered<n:
            while idx<n+1 and intervals[idx][0]<=covered:
                farthest=max(farthest,intervals[idx][1])
                idx+=1
            if farthest==covered:
                return -1
            count+=1
            covered=farthest
        return count
        