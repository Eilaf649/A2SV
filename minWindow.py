class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        answer=(0, float('inf'))
        left=0
        target=Counter(t)
        win=Counter()
        current, required= 0, len(t)
        for right in range(len(s)):
            ch=s[right]
            win[ch]+=1
            
            while all(win[c]>=target[c] for c in target):
                if answer[1]>=right-left+1:
                    answer= (left, right-left+1)
                win[s[left]]-=1
                if win[s[left]]==0:
                    del win[s[left]]
                left+=1
        if answer[1] == float("inf"): 
            return ""
        else: 
            return s[answer[0]: answer[0]+answer[1]]
 


        
