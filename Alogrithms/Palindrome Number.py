__author__ = 'responsible'
import math
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        length = int(math.log(x, 10) + 1)
        while (length > 0):
            first = x / 10 ** (length - 1)
            last = x % 10
            x %= 10 ** (length - 1)
            x /= 10
            length -= 2
            if first != last:
                return False
        return True