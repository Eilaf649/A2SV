class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts=Counter(nums)
        maj=len(nums)//2
        for num in nums:
            if counts[num]>maj:
                return num
        
