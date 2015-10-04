__author__ = 'responsible'
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        leftPtr = rightPtr = len(nums) - 1
        while leftPtr >= 0:
            if nums[leftPtr] == val:
                nums[leftPtr], nums[rightPtr] = nums[rightPtr], nums[leftPtr]
                rightPtr -= 1
            leftPtr -= 1
        return rightPtr + 1