__author__ = 'responsible'
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = "1"
        for i in xrange(n-1):
            lastChar = ans[0]
            curCharCount = 0
            newAns = ""
            for item in ans:
                if item != lastChar:
                    newAns += str(curCharCount) + lastChar
                    curCharCount = 1
                    lastChar = item
                else:
                    curCharCount += 1
            ans = newAns + str(curCharCount) + lastChar
        return ans