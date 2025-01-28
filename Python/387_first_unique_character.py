class Solution:
    def firstUniqChar(self, s: str) -> int:
        charMap = dict()

        for c in s:
            if c in charMap:
                charMap[c] += 1
            else:
                charMap[c] = 1

        for i in range(len(s)):
            if charMap[s[i]] == 1:
                return i

        return -1
