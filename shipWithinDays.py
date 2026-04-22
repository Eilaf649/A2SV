class Solution(object):
    def canship(self,n, weights, days):
        capacity=n
        num=1
        for i in range(len(weights)): 
            if (capacity-weights[i])<0:
                #print(capacity-weights[i])
                num+=1
                capacity=n
            capacity-=weights[i]
        print(n, num, num<=days)
        return num<=days
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        mini=max(weights)
        maxi=sum(weights)
        print(maxi, mini)
        left=mini
        right=maxi 
        while right>=left:
            mid=(left+right)//2
            if self.canship(mid, weights, days):
                #print('rr')
                right=mid-1
            else:
                left=mid+1
        return left
        
