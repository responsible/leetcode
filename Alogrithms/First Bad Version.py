__author__ = 'responsible'
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        leftPtr = 1
        rightPtr = n
        while rightPtr - leftPtr > 1:
            if isBadVersion((leftPtr + rightPtr) / 2):
                rightPtr = (leftPtr + rightPtr) / 2
            else:
                leftPtr = (leftPtr + rightPtr) / 2
        return filter(isBadVersion,(leftPtr,rightPtr))[0]