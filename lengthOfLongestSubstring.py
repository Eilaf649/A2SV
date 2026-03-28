class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=0
        adict=Counter()
        maxi=float('-inf')
        if s=="":
            return 0
        for right in range(len(s)):
            adict[s[right]]+=1
            while adict[s[right]]>1 and left<len(s):
                adict[s[left]]-=1
                if adict[s[left]]==0:
                    del adict[s[left]]
                left+=1
            maxi=max(right-left+1, maxi)
        return maxi













        """
        length=0
        left=0
        adict=defaultdict(int)
        max_len=0
        for right in range(len(s)):
            adict[s[right]]+=1
            while left<len(s)and len(adict)!=(right-left+1):
                adict[s[left]]-=1
                if adict[s[left]]==0:
                    del adict[s[left]]
                left+=1
            max_len=max(max_len, right-left+1)
        return max_len
        """
        """
        window_length=1
        left=0
        s=list(s)
        for right in range(1, len(s)):
            while s[right] in s[left:window_length]:
                left+=1
                print(window_length-1)
            else:
                window_length+=1
        return window_length-left
        """
                

        
