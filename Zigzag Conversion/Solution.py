class Solution(object):
    def convert(self, s, numRows):
        resList = []
        j = numRows-1
        for i in range (0, len(s)):
            if (i < numRows):
                # Creating list of strings
                resList.append(s[i])
            else:
                # Changing Directions
                if (j == numRows-1) and (j != 0):
                    forward = False
                elif (j == 0):
                    forward = True
                
                # Increment or decrement if numRows > 1
                if (numRows != 1):
                    if (forward):
                        j += 1
                    else:
                        j -= 1
                resList[j] = resList[j] + s[i]
        
        # Putting all the strings together
        res = ""
        for l in resList:
            res = res + l
            
        return res