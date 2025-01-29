from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        dirs = [(1, 0), (0, 1), (0, -1), (-1, 0)]

        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return grid[0][0]

        visited = set()

        def dfs(r, c):
            fish = 0
            if grid[r][c] == 0 or (r, c) in visited:
                return fish

            fish += grid[r][c]
            visited.add((r, c))

            for dr, dc in dirs:
                if 0 <= r + dr < m and 0 <= c + dc < n:
                    fish += dfs(r + dr, c + dc)
            return fish

        maxFish = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] != 0 and (r, c) not in visited:
                    maxFish = max(maxFish, dfs(r, c))
                else:
                    visited.add((r, c))

        return maxFish
