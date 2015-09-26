__author__ = 'responsible'
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        temp = 1
        for i in xrange(-1, -len(digits) - 1, -1):
            digits[i] = digits[i] + temp
            if digits[i] > 9:
                temp = digits[i] - 9
            else:
                temp = 0
            digits[i] %= 10
        if temp != 0:
            digits.insert(0, temp)
        return digits