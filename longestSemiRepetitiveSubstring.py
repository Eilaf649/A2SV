class Solution(object):
    def longestSemiRepetitiveSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=list(s)
        left=0
        adict=Counter()
        maxi=0
        flag=False
        pair=0
        last_pair=-1
        if len(s)==1:
            return 1
        for right in range(len(s)-1):
            if s[right]==s[right+1]:
                pair+=1
                if pair==2:
                    left=last_pair+1
                    pair=1
                last_pair=right
            maxi=max(maxi, right-left+2)
        return maxi
