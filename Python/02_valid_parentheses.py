class Solution:
    def isValid(self, s: str) -> bool:
        charmap = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        stack = []

        for char in list(s):
            if char not in charmap:
                stack.append(char)
            elif stack:
                last = stack.pop()
                if charmap[char] != last:
                    return False
            else:
                return False
                
        if stack:
            return False
        
        return True