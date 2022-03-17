class Solution(object):
    def twoSum(self, nums, target):
        index = []
        for i in range (0, len(nums)):
            num2 = target - nums[i]
            if num2 in nums:
                index2 = nums.index(num2)
                if (i != index2):
                    index.append(i)
                    index.append(index2)
                    break
        return index