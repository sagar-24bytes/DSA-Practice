class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rows=len(matrix)
        cols=len(matrix[0])
        n=rows*cols
        res=[]
        for i in range(0,rows):
            res.extend(matrix[i])
        res.sort()
        return res[k-1]

        