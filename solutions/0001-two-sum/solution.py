class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdict = {}
        for index, num in enumerate(nums):
            if (target - num) in numdict:
                return [index, numdict[target-num]]
            numdict[num] = index
