class Solution(object):
    def reverse(self, x):
        negative = False
        if (x < 0):
            negative = True
            x *= -1
        reverse = 0
        while (x > 0):
            reverse = (reverse * 10) + (x % 10)
            x = x / 10
            
        if (negative):
            reverse *= -1
        if ((reverse < -(2**31)) or (reverse > (2**31) - 1)):
            return 0
        return reverse