class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        run=[0]*len(nums)
        run[0]=nums[0]
        for i in range(1,len(nums)):
            run[i]=run[i-1]+nums[i]
        return run
        
