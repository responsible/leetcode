__author__ = 'responsible'
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        return False