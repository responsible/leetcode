# coding:utf-8
__author__ = 'responsible'
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        integer = numerator / denominator
        decimal = ""
        if integer * denominator == numerator:
            return str(integer)
        else:
            if integer < 0:
                numerator, denominator = abs(numerator), abs(denominator)
                integer = "-" + str(numerator / denominator)
            dividend = []
            numerator %= denominator
            while numerator != 0:
                if numerator not in dividend:
                    dividend.append(numerator)
                    decimal += str(numerator * 10 / denominator)
                    numerator = numerator * 10 % denominator
                else:
                    decimal = decimal[:dividend.index(numerator)] + "(" + decimal[dividend.index(numerator):] + ")"
                    break
            return str(integer) + "." + decimal