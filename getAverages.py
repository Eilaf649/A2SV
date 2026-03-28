class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # number of positive values == len(nums)-1//2
        #you use sliding window and move to get the same k at both sides so it's fixed sliding window
        arr=[-1]*len(nums)
        sumi=0
        left=0
        if k==0:
            return nums
        elif k>len(nums):
            for i in range(len(nums)):
                nums[i]=-1
            return nums

        for right in range(0, len(nums)):
            sumi+=nums[right]
            
            while right-left>2*k:
                print(left, right, sumi, nums[k+left])
                if sumi>0:
                    sumi-=nums[left]
                left+=1
            #print(k)
            if right-left+1==(2*k)+1:
                avgi=(sumi//(right-left+1))
                arr[right-k]=avgi
        return arr
