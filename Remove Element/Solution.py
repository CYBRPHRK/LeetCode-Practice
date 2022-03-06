class Solution(object):
    def removeElement(self, nums, val):
        '''
        # **Solution 1**
        i = 0
        while (i<len(nums)):
            if (nums[i] == val):
                nums[i] = nums[len(nums) - 1]
                i -= 1
                nums.remove(nums[len(nums) - 1])
            i += 1
        
        # **Solution 2**
        count = nums.count(val)
        for i in range (0, count):
            nums.remove(val)
        '''

        # **Solution 3**
        for i in range (0, nums.count(val)):
            nums.remove(val)
        return len(nums)