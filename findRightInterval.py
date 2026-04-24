class Solution(object):
    def binary(self,intervals, copy,cur, c):
        right=len(copy)-1
        left=0
        while right>left:
            mid=(left+right)//2
            
            if copy[mid][0]>=cur[1]:
                right= mid
            elif copy[mid][0]<cur[1]:
                left=mid+1
        #print(mid, left, right, curr[1], intervals[left])
        if copy[left][0]>=cur[1]:
            return intervals.index(copy[left])
        else:
            return -1
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        copy=sorted(intervals)
        ans=[]
        for i in range(len(intervals)):
            a=self.binary(intervals, copy, intervals[i],i)
            ans.append(a)
        return ans
        print(ans)
        
