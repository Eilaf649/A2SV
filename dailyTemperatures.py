class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
    
        stack=[]
        res=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                prev=stack[-1]
                res[prev]=i-prev
                stack.pop()
                #print(x)
            stack.append(i)
        #print(stack)
        return res
        
