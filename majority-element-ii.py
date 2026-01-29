class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counts= Counter(nums)
        result=[]
        maj=len(nums)//3
        for num in nums:
            if counts[num]>maj:
                result.append(num)
        result=set(result)
        result=list(result)
        return result
        
