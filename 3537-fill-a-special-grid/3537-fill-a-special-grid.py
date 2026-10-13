class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        size = 1 << n
        grid = [[0] * size for _ in range(size)]

        def fill(r, c, side, start):
            if side == 1:
                grid[r][c] = start
                return

            half = side // 2
            block = half * half

            # Required order:
            # top-right < bottom-right < bottom-left < top-left
            fill(r, c + half, half, start)
            fill(r + half, c + half, half, start + block)
            fill(r + half, c, half, start + 2 * block)
            fill(r, c, half, start + 3 * block)

        fill(0, 0, size, 0)
        return grid
