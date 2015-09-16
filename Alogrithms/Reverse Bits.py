__author__ = 'responsible'
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        reverseBinary = str(bin(int(n))[2:])
        reverseBinary = ("0" * (32-len(reverseBinary)) + reverseBinary)[::-1]
        return int(reverseBinary,2)