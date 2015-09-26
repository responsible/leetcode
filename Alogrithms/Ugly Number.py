__author__ = 'responsible'
import math
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #Key: Any number can be multiplied by some prime numbers
        if num <= 0:
            return False
        while (num % 2 == 0):
            num /= 2
        while (num % 3 == 0):
            num /= 3
        while (num % 5 == 0):
            num /= 5
        if num != 1:
            return False
        return True