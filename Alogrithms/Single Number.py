__author__ = 'responsible'
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # This problem is similar to "268 - Missing Number"
        ans = nums[0]
        for i in xrange(1,len(nums)):
            ans ^= nums[i]
        return ans