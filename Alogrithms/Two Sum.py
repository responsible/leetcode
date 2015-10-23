__author__ = 'responsible'
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        minusData = {}
        for index, item in enumerate(nums):
            if minusData.has_key(item):
                return sorted([minusData[item], index + 1])
            else:
                minusData[target - item] = index + 1