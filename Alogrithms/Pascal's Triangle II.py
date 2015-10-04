__author__ = 'responsible'
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        #k=0|    1
        #k=1|   1 1
        #k=2|  1 2 1
        #k=3| 1 3 3 1
        #  121
        # + 121
        # ------
        # =1331
        ans = [1]
        for i in xrange(rowIndex):
            ans.append(0)
            for j in xrange(i + 1, 0, -1):
                ans[j] += ans[j - 1]
        return ans