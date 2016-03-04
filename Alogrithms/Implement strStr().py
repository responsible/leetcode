__author__ = 'responsible'
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        haystack_pos = 0
        while haystack_pos <= len(haystack) - len(needle):
            if needle == haystack[haystack_pos:haystack_pos + len(needle)]:
                return haystack_pos
            haystack_pos += 1
        return -1