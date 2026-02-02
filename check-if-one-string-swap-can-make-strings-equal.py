class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1=list(s1)
        s2=list(s2)
        if s1==s2:
            return True
        for i in range(len(s1)):
            for j in range(len(s1)):
                s1[i], s1[j]=s1[j],s1[i]
                if s1==s2:
                    return True
                s1[i], s1[j]=s1[j],s1[i]
        return False
        
        
