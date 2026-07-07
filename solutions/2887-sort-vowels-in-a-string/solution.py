class Solution:
    def sortVowels(self, s: str) -> str:
        sortedS = sorted(s)
        corrli = []
        for i in range(len(sortedS)):
            if sortedS[i] in "AEIOUaeiou":
                corrli.append(i)
        
        j=0
        s = list(s)
        for i in range(len(s)):
            if s[i] in "AEIOUaeiou":
                s[i] = sortedS[corrli[j]]
                j += 1
        return "".join(s)


