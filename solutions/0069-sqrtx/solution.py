class Solution:
    def mySqrt(self, x: int) -> int:
        low = 2
        high = x//2

        if(x <2):
            return x

        while(low <= high):
            mid = (low + high) // 2
            num = mid * mid
            if (num == x):
                return mid
            elif (num < x):
                low = mid + 1
            else:
                high = mid - 1
        return high

