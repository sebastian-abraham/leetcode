class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hmaps = [0]*26
        hmapt = [0]*26

        for c in s:
            hmaps[ord(c) - ord('a')] += 1

        for c in t:
            hmapt[ord(c) - ord('a')] += 1

        return(hmaps == hmapt)


