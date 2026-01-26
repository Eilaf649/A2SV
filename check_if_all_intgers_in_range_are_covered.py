class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        tracker=0
        for i in range(left, right+1):
            for r in ranges:
                if i>= r[0] and i<=r[1]:
                    tracker+=1
                    break
        if tracker==right-left+1:
            return True
        else:
            return False
        
