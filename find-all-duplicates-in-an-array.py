class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        counts=Counter(nums)
        for key,value in counts.items():
            if value==2:
                result.append(key)
        return result
            
