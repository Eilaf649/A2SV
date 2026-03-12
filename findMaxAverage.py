class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window=0
        for i in range(k):
            window+=nums[i]
        maxi=window
        h=0
        for j in range(k, len(nums)):
            window+=nums[j]
            window-=nums[h]
            maxi=max(window, maxi)
            h+=1
            print maxi
        avg= maxi/float(k)
        return avg


        
        
