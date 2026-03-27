class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        maxi=float('-inf')
        points.sort()
        for i  in range(len(points)-1):
            dis=points[i+1][0]-points[i][0]
            maxi=max(maxi, dis)
        return maxi
