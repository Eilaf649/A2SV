class Solution(object):
    def caneat(self, piles, n, h):
        capacity=n
        num=0
        for i in range(len(piles)):
            if capacity<piles[i]:
                if piles[i]%capacity!=0:
                    num+=(piles[i]//capacity)+1
                else:
                    num+=(piles[i]//capacity)
            else:
                num+=1
        print(n, num, num<=h)
        return num<=h
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        mini=1
        maxi=max(piles)
        print(maxi, mini)
        left=mini
        right=maxi 
        while right>=left:
            mid=(left+right)//2
            if self.caneat(piles, mid, h):
                right=mid-1
            else:
                left=mid+1
            print(right, left)
        return left

        
