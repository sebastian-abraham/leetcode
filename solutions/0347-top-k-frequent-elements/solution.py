import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        minHeap = []

        for elem, frequ in freq.items():
            heapq.heappush(minHeap, (frequ, elem))

            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        li = [x[1] for x in list(minHeap)]
        return li[::-1]
