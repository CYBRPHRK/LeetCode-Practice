class Solution(object):
    def sortedSquares(self, nums):
        # Square the numbers in the list
        for i in range (0, len(nums)):
            nums[i] = nums[i] ** 2
        # Sort the list
        nums.sort()
        return nums
        