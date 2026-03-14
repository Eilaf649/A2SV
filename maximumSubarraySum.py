class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sumi=0
        left=0
        maxi=0
        adict=Counter()
        sumi=0
        for right in range(len(nums)):
            adict[nums[right]]+=1
            sumi+=nums[right]
            #print(adict, sumi, left, right, maxi)
            while left<len(nums) and (len(adict)<right-left+1 or right-left+1>k):
                #print(adict, sumi, left, right, maxi)
                adict[nums[left]]-=1
                sumi-=nums[left]
                if adict[nums[left]] == 0:
                    del adict[nums[left]]
                left+=1
                #print(adict, sumi, left, right, maxi)
            if right-left+1==k and len(adict)==right-left+1:
                maxi=max(maxi, sumi)
        return maxi
        
