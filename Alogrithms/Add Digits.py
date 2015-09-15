__author__ = 'responsible'
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num - 9*int(abs(num-1)/9)
