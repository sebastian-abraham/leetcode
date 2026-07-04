class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        peak = 0
        
        if(j == 0):
            return 0

        while( i <= j):
            print(i,nums[peak])
            if(nums[i] > nums[peak]):
                peak = i
            if(nums[j] > nums[peak]):
                peak = j
            i += 1
            j -= 1
        return peak
