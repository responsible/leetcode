__author__ = 'responsible'
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        columnNumber = 0
        for i in xrange(len(s)):
            columnNumber += int((ord(s[-i-1])-ord('A')+1) * 26**i)
        return columnNumber