__author__ = 'responsible'
import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and str(math.log(n, 3)).split('.')[1] == '0'
