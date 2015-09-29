__author__ = 'responsible'
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        try:
            for item in s:
                if item in ["(","{","["]:
                    stack.append(item)
                elif item == ")" and stack[-1] == "(" or item == "}" and stack[-1] == "{" or item == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        except:
            return False
        return len(stack) == 0