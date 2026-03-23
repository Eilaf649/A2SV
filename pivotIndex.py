class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        run_s=0
        run_p=0
        sumi_l=[0]*(len(nums)+1)
        sumi_r=[0]*(len(nums)+1)
        for j in range(len(nums)):
                run_s+=nums[j]
        sumi_r[0]=run_p
        
        for i in range(len(nums)):
            sumi_l[i]=run_p
            if i>0:
                run_p+=nums[i-1]
            sumi_r[i]=run_p
            run_s-=nums[i]
            print(run_p, run_s, i)
            if run_p==run_s:
                return i
        return -1
       
