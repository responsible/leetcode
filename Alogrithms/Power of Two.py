__author__ = 'responsible'
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1 or str(bin(n)).count("1") > 1:
            return False
        else:
            return True