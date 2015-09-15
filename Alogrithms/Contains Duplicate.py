__author__ = 'responsible'
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numTable = {}
        duplicate = False
        for num in nums:
            if numTable.has_key(num):
                duplicate = True
                break
            else:
                numTable[num] = 1
        return duplicate