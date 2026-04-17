class Solution:
    def scoreOfString(self, s: str) -> int:
        l = 0
        r = 1
        summation = 0
        for i in range(len(s) - 1):
            summation += abs(ord(s[r]) - ord(s[l]))
            l += 1
            r += 1
        return summation
