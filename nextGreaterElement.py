class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack=[]
        d={}
        for i in nums2:
            while stack and i>stack[-1]:
                key=stack.pop()
                d[key]=i
            stack.append(i)
        res=[]
        for num in nums1:
            if num in d.keys():
                res.append(d[num])
            else:
                res.append(-1)
        return res 
