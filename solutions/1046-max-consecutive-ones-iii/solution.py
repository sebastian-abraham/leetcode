class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxWind = 0
        zc = 0
        j = 0
    
        for i in range(len(nums)):
            if nums[i] == 0:
                zc += 1
                while(zc > k):
                    if nums[j] == 0:
                        zc -= 1
                    j += 1
            maxWind = max(maxWind, i+1-j)

        return maxWind
