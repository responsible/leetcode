__author__ = 'responsible'
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        while(n!=0):
            if n%2 == 1:
                ret += 1
            n /= 2
        return ret