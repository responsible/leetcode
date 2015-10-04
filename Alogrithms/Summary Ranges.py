__author__ = 'responsible'
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) < 1:
            return []
        nums += [None]
        start = prev = nums[0]
        ans = []
        for index, item in enumerate(nums):
            if index == len(nums) - 1 or item - prev > 1:
                if start == prev:
                    ans.append("%s" % start)
                else:
                    ans.append("%s->%s" % (start, prev))
                start = item
            prev = item
        return ans