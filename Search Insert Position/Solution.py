class Solution(object):
    def searchInsert(self, nums, target):
        if target not in nums:
            # if target is greater than the last element
            if (nums[len(nums)-1] < target):
                return len(nums)
            # if target is smaller than the first element
            elif (nums[0] > target):
                return 0
            for i in range (0, len(nums)-1):
                if (nums[i] < target) and (nums[i+1] > target):
                    return i+1
        # If target is in the list
        return nums.index(target)