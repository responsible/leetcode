__author__ = 'responsible'
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        #k=0|    1
        #k=1|   1 1
        #k=2|  1 2 1
        #k=3| 1 3 3 1
        #  121
        # + 121
        # ------
        # =1331
        ans = []
        row = [1]
        for i in xrange(numRows):
            ans.append(list(row))
            row.append(0)
            for j in xrange(i + 1, 0, -1):
                row[j] += row[j - 1]
        return ans