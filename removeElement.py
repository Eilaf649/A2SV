class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        zero=0
        for i in range(len(nums)):
            if nums[i]==val:
                nums[i]=0
                zero+=1
        nums.sort(reverse=True)
        for k in range(zero):
            nums.pop()
