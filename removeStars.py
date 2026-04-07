class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for i in range(len(s)):
            if s[i]=='*' and stack:
                stack.pop()
            else:
                stack.append(s[i])
        arr=""
        for j in stack:
            arr+=j
        return arr
        
