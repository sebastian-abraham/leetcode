class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tarr = [*t]
        for c in s:
            if c in tarr:
                tarr.remove(c)
            else:
                return False
        return len(tarr) == 0
