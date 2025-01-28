class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        maxLength = 1
        l, r = 0, 1

        while l < r and r < len(s) + 1:  # O(n) n = length of string
            substring = s[l:r]
            if len(substring) == len(set(substring)):  # O(n) n = length of string
                r += 1
                maxLength = max(maxLength, len(substring))
            else:
                l += 1

        return maxLength


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        maxLength = 0
        l = 0
        charSet = set()

        for r in range(len(s)):  # O(n) n = length of string
            while s[r] in charSet:  # "in" O(1)
                set.remove(s[l])  # O(1)
                l += 1
            charSet.add(s[r])  # O(1)
            maxLength = max(maxLength, r - l + 1)

        return maxLength
