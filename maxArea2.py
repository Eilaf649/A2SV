class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        maxi=float('-inf')
        arr=[]
        while i<j:
            w=j-i
            a=w*min(height[i], height[j])
            arr.append(a)
            if height[j]>height[i]:
                i+=1
            else:
                j-=1
        arr.sort(reverse=True)
        s=arr[0]
        return s
