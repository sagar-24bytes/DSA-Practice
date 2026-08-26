class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans=[]
        for x,y in points:
            d=(x**2)+(y**2)
            ans.append([[x,y],d])
        ans.sort(key= lambda x:x[1])
        res=[]
        for j in ans:
            res.append(j[0])
            if len(res)==k:
                return res
        
        