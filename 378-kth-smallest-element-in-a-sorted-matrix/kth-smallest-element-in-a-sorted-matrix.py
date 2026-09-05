import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap=[]
        n=len(matrix)
        for i in range(n):
            heapq.heappush(heap, (matrix[i][0], i, 0))
        for x in range(k):
            val,r,c=heapq.heappop(heap)

            if x==k-1:
                return val
            if c+1<n:
                heapq.heappush(heap, (matrix[r][c+1], r, c+1))
        

        