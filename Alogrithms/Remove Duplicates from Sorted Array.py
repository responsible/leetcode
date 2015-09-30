__author__ = 'responsible'
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        iter = 0
        while iter < len(nums) - 1:
            while iter < len(nums) - 1 and nums[iter] == nums[iter + 1]:
                del nums[iter + 1]
            else:
                iter += 1
        return len(nums)
