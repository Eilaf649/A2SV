class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        x=[]
        i=0
        j=len(height)-1
        while i<j:
            w=j-i
            t=min(height[j], height[i])
            x.append(w*t)
            if height[i]>=height[j]:
                j-=1
            elif height[j]>height[i]:
                i+=1
        s=max(x)
        return s
            
