import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap=[]
        for n in nums:
            heapq.heappush(heap,-n)
        for i in range(k-1):

            heapq.heappop(heap)
        print(heap)
        return -heapq.heappop(heap)