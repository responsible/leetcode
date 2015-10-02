__author__ = 'Administrator'
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for item in s.strip():
            if item == " ":
                ans = 0
            else:
                ans += 1
        return ans