__author__ = 'responsible'
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        data = {}
        for index, item in enumerate(nums):
            if data.has_key(item) == False:
                data[item] = index
            else:
                if index - data[item] <= k:
                    return True
                else:
                    data[item] = index
        return False