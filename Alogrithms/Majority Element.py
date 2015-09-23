__author__ = 'responsible'
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        data = {}
        for num in nums:
            if data.has_key(num):
                data[num] += 1
            else:
                data[num] = 1
            if data[num] > len(nums) / 2:
                return num