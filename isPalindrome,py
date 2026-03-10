class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        x=[]
        for i in s:
            if i.isalnum():
                x.append(i.lower())
        print(x)
        left=0
        right=len(x)-1
        while left<right:
            if x[left]!=x[right]:
                return False
            left+=1
            right-=1
        return True
        
