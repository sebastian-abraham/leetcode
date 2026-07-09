import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        li = defaultdict(list)
        res = []

        for elm, frequ in freq.items():
            li[frequ].append(elm)

        for i in range(len(nums), 0, - 1):
            if i in li:
                res.extend(li[i])
                if len(res) >= k:
                        return res[:k]
            

