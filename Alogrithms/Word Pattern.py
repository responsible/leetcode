__author__ = 'responsible'
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        mapping = {}
        str = str.split(" ")
        if len(pattern) != len(str):
            return False
        for i in xrange(len(pattern)):
            if mapping.has_key(pattern[i]) and mapping[pattern[i]] != str[i]:
                    return False
            else:
                mapping[pattern[i]] = str[i]
            if mapping.has_key(str[i]) and mapping[str[i]] != pattern[i]:
                return False
            else:
                mapping[str[i]] = pattern[i]
        return True
