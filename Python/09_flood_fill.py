from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        m, n = len(image), len(image[0])
        previous = image[sr][sc]

        def fill(sr, sc, color, previous):
            if sr < 0 or sr >= m:
                return
            if sc < 0 or sc >= n:
                return
            if image[sr][sc] != previous:
                return

            image[sr][sc] = color
            fill(sr + 1, sc, color, previous)
            fill(sr - 1, sc, color, previous)
            fill(sr, sc + 1, color, previous)
            fill(sr, sc - 1, color, previous)

        fill(sr, sc, color, previous)
        return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2

print(Solution().floodFill(image, sr, sc, color))
