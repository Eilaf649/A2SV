class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        sumi=0
        maxi=0
        count=Counter()
        for right in range(len(nums)):
            count[nums[right]]+=1
            sumi+=nums[right]
            while count[nums[right]]>1 and left<len(nums):
                count[nums[left]]-=1
                sumi-=nums[left]
                if count[nums[left]]==0:
                    del count[nums[left]]
                left+=1
            maxi=max(sumi, maxi)
        return maxi

        
