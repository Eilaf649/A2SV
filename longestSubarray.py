from sortedcontainers import SortedDict
class Solution(object):
       def longestSubarray(self, nums, limit):
        stack_min=deque()
        stack_max=deque()
        left=0
        mini=float('inf')
        lar=float('-inf')
        maxi=float('-inf')
        for right in range(len(nums)):
            while stack_min and stack_min[-1]>nums[right]:
                stack_min.pop()
            stack_min.append(nums[right])
            while stack_max and stack_max[-1]<nums[right]:
                stack_max.pop()
            stack_max.append(nums[right])
            while stack_max[0]-stack_min[0]>limit:
                if stack_max[0]==nums[left]:
                    stack_max.popleft()
                elif stack_min[0]==nums[left]:
                    stack_min.popleft()
                left+=1
            maxi=max(maxi, right-left+1)
        return maxi
