__author__ = 'responsible'
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = self.getVersion(version1)
        version2 = self.getVersion(version2)
        if len(version1) > len(version2):
            version2 += [0 for i in xrange(len(version1)-len(version2))]
        elif len(version1) < len(version2):
            version1 += [0 for i in xrange(len(version2)-len(version1))]
        for item in xrange(max(len(version1),len(version2))):
            if version1[item] > version2[item]:
                return 1
            if version1[item] < version2[item]:
                return -1
        return 0

    def getVersion(self,version):
            return map(int,version.split("."))