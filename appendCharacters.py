class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        j=0
        i=0
        while j<len(s) and i<len(t):
            if s[j]==t[i]:
                i+=1
            j+=1
        res=len(t)-i
        return  res
