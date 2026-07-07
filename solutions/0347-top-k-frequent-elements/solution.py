class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        li = sorted(freq, key = lambda k: freq[k], reverse = True)
        
        return li[:k]
