class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #nums.sort()
        right=len(nums)-1
        left=0
        while right>=left:
            mid=(right+left)//2
            print(mid, left, right)
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1
     
        
