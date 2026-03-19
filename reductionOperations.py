class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        up=0
        res=0
        for i in range(1, len(nums)):
            if nums[i]!=nums[i-1]:
                up+=1
                print(nums, nums[i], nums[i-1],up)
            res+=up
            print(res)
        return res
        
