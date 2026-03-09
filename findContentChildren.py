class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        count=0
        j=0
        s.sort()
        g.sort()
        for i in range(len(g)):
            flag=False
            while flag!=True and j<len(s):
                if s[j] >= g[i]:
                    count+=1
                    flag=True
                j+=1
        return count
