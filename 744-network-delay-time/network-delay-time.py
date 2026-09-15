import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=[[] for _ in range(n+1)]
        for u,v,w in times:
            graph[u].append([v,w])
        dist=[float('inf')]*(n+1)
        dist[0]=0
        dist[k]=0
        heap=[]
        heapq.heappush(heap,(0,k))

        while heap:
            d,node=heapq.heappop(heap)
            for nei,w in graph[node]:
                if d+w <dist[nei]:
                    dist[nei]=d+w
                    heapq.heappush(heap,(dist[nei], nei ))
        for j in dist:
            if j==float('inf'):
                return -1
        return max(dist)




        