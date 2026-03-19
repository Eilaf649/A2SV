class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        left=0
        res=[]
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                if nums[left]+nums[right]+nums[i]==0:
                    if [nums[i],nums[left],nums[right]] not in res:
                        res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                elif nums[left]+nums[right]+nums[i]>0:
                    right-=1
                else:
                    left+=1
            print(nums[i],nums[left], nums[right])
        return res
