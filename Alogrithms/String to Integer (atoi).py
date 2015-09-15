__author__ = 'responsible'
import re
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = re.sub(re.compile("\\s*"),"",str,1)
        ret = re.match(re.compile("([+-]{0,1}\\d*)\\D*"),str)
        if ret == None or ret.group(1) in ["","+","-"]:
            return 0
        else:
            ret = int(ret.group(1))
            if ret > 2**31-1:
                return 2**31-1
            elif ret < -2**31:
                return -2**31
            else:
                return ret