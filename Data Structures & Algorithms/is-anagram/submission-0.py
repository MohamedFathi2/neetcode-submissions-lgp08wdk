class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) < len(t) or len(s) > len(t):
            return False
        sDic = {}
        tDic = {}
        for c in s:
            if c in sDic:
                sDic[c] += 1
            else:
                sDic[c] = 1
        for c in t:
            if c in tDic:
                tDic[c] += 1
            else:
                tDic[c] = 1
        return sDic == tDic