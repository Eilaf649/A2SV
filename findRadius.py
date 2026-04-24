class Solution(object):
    def binarymin(self, arr, i):
        right=len(arr)-1
        left=0
        while right>left:
            mid=(left+right)//2
            if arr[mid]>=i:
                right=mid
            else:
                left=mid+1
        return left

    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        a=[]
        heaters.sort()
        ans=float('-inf')
        for i in range(len(houses)):
            x=[]
            a=self.binarymin(heaters, houses[i])
            print(a)
            if a==0 or a==len(heaters):
                x=abs(houses[i]-heaters[a])
            else:
                x=min(abs(houses[i]-heaters[a]), (abs(houses[i]-heaters[a-1])))
            print(ans)
            ans=max(ans, x)
        return ans
         
