class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        for i in range(len(nums)):
            counts=0
            for j in range(len(nums)):
                if nums[j]<nums[i] and j!=i:
                    counts+=1
            result.append(counts)
        return result
        
