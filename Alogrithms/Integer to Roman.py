__author__ = 'responsible'
import math
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Symbol Value(Wikipedia:Roman numerals)
        # I	     1
        # V	     5
        # X	     10
        # L	     50
        # C	     100
        # D	     500
        # M	     1,000
        # ...    ...
        # CD     400
        # CM     900
        # DM     500
        # ...    ...
        rule = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        ans = ""
        if rule.has_key(num):
            return rule[num]
        while num > 0:
            E = 10 ** int(math.log(num, 10))
            digit = num / E
            if rule.has_key(digit * E):
                ans += rule[digit * E]
            elif 0 < digit < 4:
                ans += rule[E] * digit
            elif digit == 4:
                ans += rule[E] + rule[5 * E]
            elif 5 < digit < 9:
                ans += rule[5 * E] + rule[E] * (digit - 5)
            elif digit == 9:
                ans += rule[E] + rule[10 * E]
            num %= E
        return ans