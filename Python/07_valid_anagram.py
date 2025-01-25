from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        data = defaultdict(int)
        for char in list(s):
            data[char] += 1
        for char in list(t):
            data[char] -= 1

        return all(val == 0 for val in data.values())

        