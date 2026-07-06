class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        wind = 0
        maxWind = 0
    
        for i in nums:
            if i != 1:
                wind = 0
            else:
                wind += 1
            maxWind = max(maxWind, wind)

        return maxWind
