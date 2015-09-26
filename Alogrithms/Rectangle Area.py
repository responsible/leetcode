__author__ = 'responsible'
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        crossHeight = abs(sorted((A, E, C, G))[1] - sorted((A, E, C, G))[2])
        crossWidth = abs(sorted((D, H, B, F))[1] - sorted((D, H, B, F))[2])
        rect1Area = (C - A) * (D - B)
        rect2Area = (G - E) * (H - F)
        crossArea = crossHeight * crossWidth
        if E >= C or G <= A or H <= B or F >= D:
            crossArea = 0
        return rect1Area + rect2Area - crossArea