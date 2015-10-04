__author__ = 'responsible'
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        ans = ""
        for i in xrange(len(strs[0])):
            ans += strs[0][i]
            for item in strs:
                if len(item) < i + 1 or item[i] != ans[i]:
                    return ans[0:-1]
        return ans