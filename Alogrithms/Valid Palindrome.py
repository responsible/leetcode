__author__ = 'responsible'
import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(re.compile("[^a-zA-Z0-9]"),"",s).lower()
        if len(s) & 1 == 0:
            return s[0:len(s)/2]==s[-1:-len(s)/2-1:-1]
        else:
            return s[0:(len(s)-1)/2]==s[-1:-(len(s)-1)/2-1:-1]