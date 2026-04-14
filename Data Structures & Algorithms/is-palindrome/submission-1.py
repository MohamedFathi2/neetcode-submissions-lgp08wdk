class Solution:
    def filterString(self, s: str) -> str:
        t = ""
        for c in s:
            if c.isalnum():
                t += c.lower()
        return t
    def isPalindrome(self, s: str) -> bool:
        s = self.filterString(s)
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True