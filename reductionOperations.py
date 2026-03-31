class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=[]
        count=0
        a=0
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                a+=1
            count+=a
        return count
              
