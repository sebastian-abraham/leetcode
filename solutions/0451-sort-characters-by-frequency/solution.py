class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)

        li = sorted(freq, key = lambda x: freq[x], reverse=True)
        s = ""
        for elm in li:
            s = s + elm*freq[elm]
        return s
