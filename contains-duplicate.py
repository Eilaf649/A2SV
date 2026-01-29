class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counts= Counter(nums)
        for num in nums:
            if counts[num]>1:
                return True
        return False
        
