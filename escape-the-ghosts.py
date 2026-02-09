class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        for ghost in ghosts:
            x=abs(target[0]-ghost[0])
            y=abs(target[1]-ghost[1])
            if (x+y)<=(abs(target[0])+abs(target[1])):
                return False
        return True

        
