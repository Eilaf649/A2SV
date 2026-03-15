class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowel="ioeua"
        left=0
        maxi=0
        char=[]
        length=0
        for right in range(len(s)):
            if s[right] in vowel:
                length+=1
                char=s[right]
            if right-left+1>k and  left<len(s) :
                if s[left] in vowel:
                    length-=1
                left+=1
            maxi=max(maxi, length)
        return maxi
