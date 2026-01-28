class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        player= set(chain(*matches))
        losses=Counter(y for _ ,y in matches)
        x=[x for x in player if losses[x]==0]
        y=[y for y in player if losses[y]==1]
        res=[x,y]
        return res
