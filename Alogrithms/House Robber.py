__author__ = 'responsible'
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # house[0] = nums[0]
        # house[1] = max(nums[0], nums[1])
        # house[n] = max(nums[n] + house[n-2], house[n-1])
        if len(nums) == 0: return 0
        if len(nums) <= 2: return max(nums)
        house = [nums[0], max(nums[0], nums[1])]
        for i in xrange(2, len(nums)):
            house.append(max(nums[i] + house[i - 2], house[i - 1]))
        return house[-1]
