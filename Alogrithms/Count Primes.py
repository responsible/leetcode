__author__ = 'responsible'
import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        primeArray = [True] * n
        for i in xrange(2, int(math.sqrt(n)) + 1):
            if primeArray[i] == True:
                for j in xrange(i ** 2, n, i):
                    primeArray[j] = False
        return len(filter(lambda x: x, primeArray)) - 2  # del 0 and 1 from primeArray