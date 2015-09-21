__author__ = 'responsible'
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        leftPtr , rightPtr =  0,0
        while rightPtr < len(nums):
            if nums[rightPtr] != 0:
                nums[leftPtr] , nums[rightPtr] = nums[rightPtr] , nums[leftPtr]
                leftPtr += 1
            rightPtr += 1