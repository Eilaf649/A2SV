class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        mini=float('inf')
        sumi=0
        left=0
        total_pts=sum(cardPoints)
        for right in range (len(cardPoints)):
            sumi+=cardPoints[right]
            while (right-left+1)> len(cardPoints)-k:
                sumi-=cardPoints[left]
                left+=1
                print (sumi, mini)
            if right-left+1==len(cardPoints)-k:
                mini=min(mini, sumi)
        return total_pts-mini
