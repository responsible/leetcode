__author__ = 'responsible'
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mappingS = {}
        mappingT = {}
        for i in xrange(len(s)):
            if mappingS.has_key(s[i]) == False:
                mappingS[s[i]] = t[i]
            else:
                if mappingS[s[i]] != t[i]:
                    return False
            if mappingT.has_key(t[i]) == False:
                mappingT[t[i]] = s[i]
            else:
                if mappingT[t[i]] != s[i]:
                    return False
        return True