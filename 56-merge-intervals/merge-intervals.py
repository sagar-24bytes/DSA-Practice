class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start=intervals[0][0]
        last=intervals[0][1]
        n=len(intervals)
        ans=[]
        if n<=1:
            return intervals
        for i in range(n):
            a=intervals[i][0]
            b=intervals[i][1]
            if last<a:
                ans.append([start,last])
                start=a
            if b>last:
                last=b
        ans.append([start,last])
        return ans 
          
        