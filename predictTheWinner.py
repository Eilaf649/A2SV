class Solution(object):
    def greed(self, nums, right, left):
        if left==right:
            return nums[right]
        return max(nums[left]-self.greed(nums,right, left+1), nums[right]-self.greed(nums, right-1, left))

    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.greed(nums, len(nums)-1, 0)>=0





        
