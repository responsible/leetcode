__author__ = 'responsible'
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left,right = 0,x
        while(right - left > 1E-9):
            ans = (left + right) / 2.0
            if ans**2 > x:
                right = ans
            else:
                left = ans
        return int(right)