class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans=[]
        maxi=float('-inf')
        q=deque()
        count=0
        left=0
        for right in range(len(nums)):
            if q and q[0]<=right-k:
                q.popleft()
                #print(left, right)
            while q and nums[q[-1]]<=nums[right]:
                q.pop()
            q.append(right)
            
            #print(q)
            if right>=k-1:
                ans.append(nums[q[0]])
        return ans




        """
        ans=[]
        left=0
        maxi=float('-inf')
        for right in range(len(nums)):

            if nums[right]>maxi:
                maxi=nums[right]
            while right-left+1>k:
                if maxi==nums[left]:
                    maxi=self.nextgreator(nums, left+1, right, maxi)
                left+=1
                
            #print(left, right)
            #print(nums[left:right+1])
            if right-left+1==k:
                #print(nums[left:right+1])
                ans.append(maxi)
        return ans
        """
        
