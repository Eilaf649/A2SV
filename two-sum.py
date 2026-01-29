lass Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices=[]
        for index1, i in enumerate(nums):
            for index2, j in enumerate(nums):
                if (index1==index2) or (j!=target-i):
                    continue
                else:
                    res= [index1, index2]
                    res.sort()
                    return res
