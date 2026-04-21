class Solution(object):
    def first(self, nums, target):
        right=len(nums)-1
        left=0
        while right>=left:
            mid=(right+left)//2  
            if nums[mid]==target:
                if mid==0 or nums[mid-1]!=target:
                    return mid
                else:
                    right=mid-1
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1
    def last(self, nums, target):
        right=len(nums)-1
        left=0
        while right>=left:
            mid=(right+left)//2  
            if nums[mid]==target:
                if mid==len(nums)-1 or nums[mid+1]!=target:
                    return mid
                else:
                    left=mid+1
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first1=self.first(nums, target)
        last1=self.last(nums, target)
        return[first1, last1]
         
