class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        def key(s):
            return (len(s), s)

        heap = []
        for s in nums:
            item = key(s)
            if len(heap) < k:
                heapq.heappush(heap, (item, s))
            elif item > heap[0][0]:
                heapq.heapreplace(heap, (item, s))

        return heap[0][1]
