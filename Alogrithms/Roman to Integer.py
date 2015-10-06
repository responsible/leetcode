__author__ = 'responsible'
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
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
        # CM     900
        # DM     500
        # ...    ...
        rule = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        return sum(map(lambda x:rule[x[0]] if rule[x[0]] >= rule[x[1]] else -rule[x[0]],zip(s,s[1:] + "I")))
