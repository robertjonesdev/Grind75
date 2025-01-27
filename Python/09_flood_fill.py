from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        m, n = len(image), len(image[0])
        previous = image[sr][sc]
        visited = set()

        def fill(sr, sc, color, previous):
            if sr < 0 or sr >= m:
                return
            if sc < 0 or sc >= n:
                return
            if image[sr][sc] != previous:
                return
            if (sr, sc) in visited:
                return

            image[sr][sc] = color
            visited.add((sr, sc))
            fill(sr + 1, sc, color, previous)
            fill(sr - 1, sc, color, previous)
            fill(sr, sc + 1, color, previous)
            fill(sr, sc - 1, color, previous)

        fill(sr, sc, color, previous)
        return image
