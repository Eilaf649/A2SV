class Solution(object):
    def binary(self, nums, target, left, right):
        while right>=left:
            mid=(right+left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return -1
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        right=len(nums)-1
        left=0
        while right>left:
            mid=(right+left)//2
            if nums[mid]>nums[right]:
                left=mid+1
                            
            else:
                right=mid
    
                
                
        l=left
    
        x= self.binary(nums, target, 0, l-1)
        print(0,l-1)
        if x!=-1:
            return x
        y= self.binary(nums, target, l, len(nums)-1)
        print(l,len(nums)-1)
        if y!=-1:
            return y
        return -1


        
       
