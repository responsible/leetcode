__author__ = 'responsible'
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Because for a number x : x^int^int == x (^ is XOR)
        # if 2 is not in a array[3,1,0] whose length is 3
        # then ans = 3^0^3^1^1^2^0 = 2
        ans = len(nums)
        for i in xrange(0, len(nums)):
            ans = ans ^ i ^ nums[i]
        return ans