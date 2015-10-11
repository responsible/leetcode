__author__ = 'responsible'
class Solution(object):
    def __init__(self):
        self.memoryData = {}
    def uniquePaths(self, m, n, x=1, y=1):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if x > m or y > n:
            return 0
        if (x, y) == (m, n):
            return 1
        if not self.memoryData.has_key((x, y)):
            self.memoryData[(x, y)] = self.uniquePaths(m, n, x + 1, y) + self.uniquePaths(m, n, x, y + 1)
        return self.memoryData[(x, y)]