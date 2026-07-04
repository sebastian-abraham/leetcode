class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums)-1

        if(j + 1 == 0):
            return 0
        
        if(j == 0 and nums[j] == val):
            return 0
        elif(j == 0 and nums[j] != val):
            return 1

        while(nums[j] == val and j ==0):
            j -= 1

        while(i <= j):
            if(nums[i] == val):
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i += 1
        return i
            
            

