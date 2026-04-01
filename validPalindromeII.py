class Solution(object):
    def isPalindrome(self, s, l ,r):
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=list(s)
        left=0
        right=len(s)-1
        count=0
        Flag=False
        while left<right:
            if s[left]!=s[right] and s[left]==s[right-1] and Flag==False and s[right]==s[left+1] and len(s)>2:
                return self.isPalindrome(s,left,right-1) or self.isPalindrome(s,left+1,right)
            elif s[left]!=s[right] and s[right]==s[left+1] and Flag==False:
                left+=1
                Flag=True
            elif s[left]!=s[right] and s[left]==s[right-1] and Flag==False:
                right-=1
                Flag=True
            elif s[left]!=s[right] and right-left>1:
                print(s[left], s[right], left, right, Flag)
                return False
            else:
                left+=1
                right-=1
        return True

