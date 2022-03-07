class Solution(object):
    def search(self, nums, target):
        begin = 0
        end = len(nums)-1
        while (begin <= end):
            mid = (begin + end)//2
            if (nums[mid] == target):
                return mid
            if (nums[mid] < target):
                begin = mid + 1
            else:
                end = mid - 1

        '''
        # Easiest Solution but not Binary Search
        if target in nums:
            return nums.index(target)
        '''
        return -1