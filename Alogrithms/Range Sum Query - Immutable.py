# coding:utf-8
__author__ = 'responsible'
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sumarray = [sum(nums[:rangesum + 1]) for rangesum in xrange(len(nums))]


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumarray[j] - self.sumarray[i - 1] if i != 0 else self.sumarray[j]



# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)