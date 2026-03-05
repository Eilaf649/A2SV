class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        """
        counts=0
        i=0
        j = len(nums)-1
        nums.sort()
        while i<j:
            if nums[i]+nums[j]==k:
                counts+=1
                i+=1
                j-=1
            elif nums[i]+nums[j]<k:
                i+=1
            elif nums[i]+nums[j]>k:
                j-=1
        return counts
