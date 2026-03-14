class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.atMost(nums, k)-self.atMost(nums, k-1)
    def atMost(self, nums, k):
        left=0
        subarrays=0
        window_size=0
        for right in range(len(nums)):
            if nums[right]%2==1:
                window_size+=1
            while window_size>k:
                if nums[left]%2==1:
                    window_size-=1
                left+=1
            subarrays+=right-left+1
        return subarrays
                   
        
