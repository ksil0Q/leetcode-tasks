class Solution(object):
    def minCostToMoveChips(self, pos):
        """
        :type position: List[int]
        :rtype: int
        """
        return min(len([1 for p in pos if p % 2 == 0]), len([1 for p in pos if p % 2 == 1]))