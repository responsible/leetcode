__author__ = 'responsible'
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        if x < 0:
            ans = int("-" + str(-x)[::-1])
        else:
            ans = int(str(x)[::-1])
        if ans > 2**31 or ans < -2**31:
            return 0
        else:
            return ans
