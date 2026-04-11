class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        d={}
        stack=[]
        arr=[]
        for i in range(2*len(nums)):
            idx=i
            while stack and nums[stack[-1]]<nums[i%len(nums)]:
                key=stack.pop()
                #if key in d.keys():
                    #arr.append([key, nums[i%len(nums)]])
                d[key]=i%len(nums)
                    #print(d, stack, i%len(nums))
            stack.append(i%len(nums))
        print(arr)
        for i in range(len(nums)):
            if i in d.keys():
                ans.append(nums[d[i]])
            else:
                ans.append(-1)
        return ans
        
