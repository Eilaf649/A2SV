class Solution(object):
    def recurr(self, s, right, left):
        if left>right:
            return
        print(left, right)
        s[left], s[right]=s[right], s[left]
        return self.recurr(s, right-1, left+1)

    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s=self.recurr(s, len(s)-1, 0)
        
        """
        for i in range(len(s)//2):
            s[i], s[len(s)-i-1]= s[len(s)-i-1], s[i]
        """    

        
