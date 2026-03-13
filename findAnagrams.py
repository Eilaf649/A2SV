class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        left=0
        tar=Counter(p)
        ans=Counter(s[:len(p)-1])
        x=[]
        for right in range(len(p)-1, len(s)):
            ans[s[right]]+=1
            if tar==ans:
                x.append(left)
            ans[s[left]]-=1
            if ans[s[left]]==0:
                del ans[s[left]]
            left+=1
            
        return x
            


        
