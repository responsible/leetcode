__author__ = 'responsible'
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        vis = {}
        while (True):
            ans = sum(map(lambda x:int(x)**2,str(n)))
            if ans == 1:
                return True
            if vis.has_key(ans):
                return False
            else:
                vis[ans] = True
            n = ans