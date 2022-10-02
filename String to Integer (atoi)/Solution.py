class Solution(object):
    def myAtoi(self, s):
        # Removing all the leading whitespaces.
        s = s.lstrip()
        
        # Returning 0 if the string is empty
        if (len(s) == 0):
            return 0
        
        # Setting isNegative to 'False' by default
        isNegative = False
        
        # Setting isNegative to 'True' and remove the sign if the first character is '-'
        if (s[0] == '-'):
            isNegative = True
            s = s[1:]
        # Removing the sign if the first character is '+'
        elif (s[0] == '+'):
            s = s[1:]
        
        # Extracting and converting the digits from the string 
        num = 0
        for i in s:
            if (i.isdigit()):
                num = num * 10 + int(i)
            else:
                break
        
        # Changing the number back to negative if it was negative in the string
        if (isNegative):
            num *= -1
        
        # Clamping the integer so that it remains in the range
        if (num > (2**31) - 1):
            num = (2**31) - 1
        elif (num < -(2**31)):
            num = -(2**31)
        
        return num