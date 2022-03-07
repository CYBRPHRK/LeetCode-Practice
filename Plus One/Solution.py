class Solution(object):
    def plusOne(self, digits):
        i = -1
        digits[i] += 1
        while (digits[i] > 9):
            digits[i] = digits[i] % 10
            i -= 1
            if (-i <= len(digits)):
                digits[i] += 1
            else:
                digits.insert(0, 1)
        
        return digits