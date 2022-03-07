class Solution(object):
    def lengthOfLastWord(self, s):
        # Removing whitespaces from front and back
        s = s.strip()
        # Splitting the words from the string and saving them in a list called 'data' 
        data = s.split(" ")

        # returning the length of the last item in the list 'data'
        return len(data[-1])