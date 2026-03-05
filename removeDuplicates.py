class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=Counter(nums)
        for i in nums:
            if c[i]>1:
                for _ in range(c[i]-1):
                    nums.remove(i)
        
