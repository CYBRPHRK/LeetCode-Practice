class Solution(object):
    def longestPalindrome(self, s):
        if (s == s[::-1]):
            return s
        longest = ""
        '''
        # **Solution 1 (Takes too long)**
        for i in range (0, len(s)):
            for j in range (len(s)-1, i, -1):
                if (s[i:j] == s[i:j][::-1]):
                    longest = longest if len(longest) >= len(s[i:j]) else s[i:j]
                    
                if (s[len(s)-1-j:len(s)-i] == s[len(s)-1-j:len(s)-i][::-1]):
                    longest = longest if len(longest) >= len(s[len(s)-1-j:len(s)-i]) else s[len(s)-1-j:len(s)-i]
        '''

        # **Solution 2**
        for i in range(0, len(s)):
            palindrome = ""
            j = 0
            # Looking for a palindrome of odd length
            while (i-j >= 0) and (i+j < len(s)) and (s[i-j] == s[i+j]):
                palindrome = s[i-j:i+j+1]
                j += 1
            
            longest = longest if len(longest) >= len(palindrome) else palindrome
            
            j = 0
            # Looking for a palindrome of even length
            while (i-j >= 0) and (i+j+1 < len(s)) and (s[i-j] == s[i+j+1]):
                palindrome = s[i-j:i+j+2]
                j += 1
                
            longest = longest if len(longest) >= len(palindrome) else palindrome

        return longest
