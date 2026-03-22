class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strs = ''
        for i in digits:
            strs += str(i)
        strs = int(strs)
        strs += 1
        return [int(i) for i in str(strs)]
