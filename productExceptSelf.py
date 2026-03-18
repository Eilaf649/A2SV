class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre=[1]*(len(nums))
        for j in range(1,len(nums)):
            pre[0]*=nums[j]
        for i in range(1,len(nums)):
            if nums[i]!=0:
                pre[i]=(pre[i-1]*nums[i-1])/nums[i]
            else:
                for u in range(len(nums)):
                    if u!=i:
                        pre[i]*=nums[u]
        return pre        
