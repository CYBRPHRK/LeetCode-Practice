class Solution(object):
    def addBinary(self, a, b):
        i = 0
        carry = 0
        a = a[::-1]
        b = b[::-1]
        sum = ""
        while ((i < len(a)) and (i < len(b))):
            if ((a[i] == '1') and (b[i]) == '1'):
                c = 0 + carry
                carry = 1
            elif (((a[i] == '0') and (b[i]) == '1') or ((a[i] == '1') and (b[i]) == '0')):
                if (carry == 1):
                    c = 0
                else:
                    c = 1
            else:
                if (carry == 1):
                    c = 1
                    carry = 0
                else:
                    c = 0
                    
            sum += str(c)
            i += 1
        
        if (i < len(a)):
            while (i < len(a)):
                #if ((a[i] == '1') and (carry == 1)):
                    #c = 0
                if ((a[i] == '0') and (carry == 1)):
                    c = 1
                    carry = 0
                elif ((a[i] == '1') and (carry == 0)):
                    c = 1
                else:
                    c = 0
                sum += str(c)
                i += 1
                    
        if (i < len(b)):
            while (i < len(b)):
                #if ((b[i] == '1') and (carry == 1)):
                    #c = 0
                if ((b[i] == '0') and (carry == 1)):
                    c = 1
                    carry = 0
                elif ((b[i] == '1') and (carry == 0)):
                    c = 1
                else:
                    c = 0
                sum += str(c)
                i += 1
        
        if (carry == 1):
            sum += '1'
            
        return sum[::-1]