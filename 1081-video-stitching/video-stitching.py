class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        covered=0
        count=0
        i=0
        farthest=0
        while covered<time:
            while i<len(clips) and clips[i][0]<=covered:
                farthest=max(farthest,clips[i][1])
                i+=1
            if farthest == covered:
                return -1
            count+=1
            covered=farthest
        return count
        