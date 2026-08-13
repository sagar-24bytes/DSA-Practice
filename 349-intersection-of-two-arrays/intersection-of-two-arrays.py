class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen={}
        for n in nums1:
            seen[n]=1
        for n in nums2:
            if n in seen:
                seen[n]+=1
        ans=[]
        for x,y in seen.items():
            if y>=2:
                ans.append(x)
        return ans 
        