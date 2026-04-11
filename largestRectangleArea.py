class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack=[]
        n=len(heights)
        maxi=float('-inf')
        left=[-1]*n
        right=[n]*n
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                left[i]=stack[-1]
            else:
                left[i]=-1
            stack.append(i)
        stack=[]
        print(left)
        for j in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[j]:
                stack.pop()
            if stack:
                right[j]=stack[-1]
            else:
                right[j]=n
            stack.append(j)
        print(right)
        for k in range(n):
            width=(right[k]-left[k]-1)
            maxi=max(maxi,width*heights[k])
        return maxi

            




         
