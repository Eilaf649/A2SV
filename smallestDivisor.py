class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """

        left=1
        right=max(nums)
        while right>left:
            mid=(left+right)//2
            a=0
            for i in nums:
                if i%mid==0:
                    a+=i//mid
                else:
                    a+=(i//mid)+1
            print(left, right, mid, a)
            if a<=threshold:
                right=mid
            else:
                left=mid+1
        return left


        
