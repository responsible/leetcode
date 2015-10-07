__author__ = 'responsible'
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        nums[:] = [nums[i % -len(nums)] for i in xrange(-len(nums) - k, - k)]