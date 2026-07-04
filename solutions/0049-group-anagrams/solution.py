from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt  = defaultdict(list)

        for stri in strs:
            dictt["".join(sorted(stri))].append(stri)
        
        return list(dictt.values())
