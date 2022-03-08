class Solution(object):
    def rotate(self, nums, k):
        # If k is greater than the length of the list, then reduce k to the least amount of rotations needed
        if (k > len(nums)):
            k = k % len(nums)
        
        # Taking the number of elements to be shifted
        res = nums[:-k]
        # Deleting the elements to be shifted from the end of the list
        del nums[:-k]
        # Shift the elements by adding them to the end of the list
        nums.extend(res)