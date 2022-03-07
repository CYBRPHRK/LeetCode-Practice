class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        i = 0
        j = 0
        while (i < len(nums1)) and (j < len(nums2)):
            if (nums1[i] >= nums2[j]):
                nums1.insert(i, nums2[j])
                j += 1
            i += 1
        
        while (j < len(nums2)):
            nums1.insert(i, nums2[j])
            i += 1
            j += 1
        
        length = len(nums1)
        if (length % 2 == 0):
            median = float (nums1[(length/2)-1] + nums1[(length/2)]) / 2
        else:
            median = nums1[(length-1)/2]
        
        return median