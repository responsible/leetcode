__author__ = 'responsible'
class Solution(object):
    memorySolution = {}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        if self.memorySolution.has_key(n):
            return self.memorySolution[n]
        else:
            self.memorySolution[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.memorySolution[n]