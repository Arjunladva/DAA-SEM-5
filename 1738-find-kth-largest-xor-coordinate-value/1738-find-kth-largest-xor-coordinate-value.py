class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        px = [[0] * (n + 1) for _ in range(m + 1)]
        heap = []

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                px[i][j] = (
                    px[i - 1][j]
                    ^ px[i][j - 1]
                    ^ px[i - 1][j - 1]
                    ^ matrix[i - 1][j - 1]
                )

                value = px[i][j]
                if len(heap) < k:
                    heapq.heappush(heap, value)
                elif value > heap[0]:
                    heapq.heapreplace(heap, value)

        return heap[0]
