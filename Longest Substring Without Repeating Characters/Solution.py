class Solution(object):
    def lengthOfLongestSubstring(self, s):
        distinct = []
        length = 0
        for c in s:
            if c not in distinct:
                distinct.append(c)
            else:
                length = length if length >= len(distinct) else len(distinct)
                del distinct[:distinct.index(c) + 1]
                distinct.append(c)
                
        return length if length >= len(distinct) else len(distinct)