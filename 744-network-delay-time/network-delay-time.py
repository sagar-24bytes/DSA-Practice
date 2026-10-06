import heapq
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph=[[] for _ in range(n+1)]
        for u,v,w in times:
            graph[u].append([v,w])
        dist=[float('inf')]*(n+1)
        dist[0]=dist[k]=0
        heap=[(0,k)]

        while heap:
            d,node=heapq.heappop(heap)
            for nei,w in graph[node]:
                if dist[nei]>d+w:
                    dist[nei]=d+w
                    heapq.heappush(heap,(dist[nei],nei))
        ans=max(dist)
        
        return ans if ans!=float('inf') else -1

        