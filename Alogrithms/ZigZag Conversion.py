__author__ = 'responsible'
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Example:
        # A					K					U	|0,10,20
        # B				J	L				T	V	|1,9,11,19,21
        # C			I		M			S		W	|2,8,12,18,22
        # D		H			N		R			X	|3,7,13,17,23
        # E	G				O	Q				Y	|4,6,14,16,24
        # F					P					Z	|5,15,25
        if numRows == 1:
            return s
        ans = ""
        for i in xrange(numRows):
            for j in xrange(i, len(s), numRows * 2 - 2):
                ans += s[j]
                ans += s[j + (numRows - i - 1) * 2] if i not in [0, numRows - 1] and j + (numRows - i - 1) * 2 < len(s) else ""
        return ans