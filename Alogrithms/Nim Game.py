__author__ = 'responsible'
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # you will win if the last turn you leave 4-7 stones for him
        return n % 4 != 0