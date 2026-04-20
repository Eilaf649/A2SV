class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for i in range(len(s)):
            if not s[i].isdigit():
                stack.append(s[i])
            else:
                stack.pop()
        ans="" 
        for j in stack:
            ans+=j
        return ans
