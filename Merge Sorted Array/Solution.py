class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if (n == 0):
            return
        if (m == 0):
            for i in range (0, n):
                nums1[i] = nums2[i]
            return

        # Position in List num1
        pos1 = 0
        # Position in List num2
        pos2 = 0
        
        # Merging the Lists
        for i in range (0, len(nums1)):
            # if nums2 list is finished, then break the loop.
            if (pos2 == n):
                break
            # If the non-zero integers in nums1 list are finished, just put the remaining nums2 list integers at the end of nums1
            elif (pos1 == m):
                nums1[i] = nums2[pos2]
                pos2 += 1
            # If the current integer in nums1 is greater than the integer at position pos2 in nums2, then insert the integer from nums2 to the current position in nums1
            elif (nums1[i] > nums2[pos2]):
                nums1.insert(i, nums2[pos2])
                nums1.pop()
                pos2 += 1
            else:
                pos1 += 1