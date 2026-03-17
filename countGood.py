class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        for right in range(len(nums)):
            if nums[right] not in adict:
                adict[nums[right]]=0
            k-=adict[nums[right]]
            adict[nums[right]]+=1
            #print(nums[left], nums[right], left, right, adict, pairs)
            #print(nums[left], nums[right], left, right, adict, pairs, subarray, nums[left: right+1])
            while (k<=0) and left<len(nums):
                adict[nums[left]]-=1
                k+=adict[nums[left]]
                left+=1
            subarray+=left
            #print(nums[left], nums[right], left, right, adict, pairs, subarray, nums[left: right+1])
        return subarray

        
