__author__ = 'responsible'
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        data = {}
        ans = []
        for num in nums:
            if data.has_key(num):
                data[num] += 1
            else:
                data[num] = 1
            if len(nums) / 3 < data[num] <= len(nums) / 3 + 1 :
                ans.append(num)
        return list(ans)