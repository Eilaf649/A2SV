class Solution(object):
    def canplace(self, position, mid, m):
        h=1
        prev=position[0]
        for j in range(1,len(position)):
            curr=position[j]
            if curr-prev>=mid:
                h+=1
                prev=curr
            if h==m:
                return True
 
        return False


           

    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()
        right=int(position[-1] / (m - 1.0)) + 1
        left=1
        answer=0
        while left<=right:
            mid = left + (right - left) // 2
            if self.canplace(position, mid, m):
                answer=mid
                left=mid+1
            else:
                right=mid-1
        return answer
