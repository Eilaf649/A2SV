class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        left=0
        count=Counter(s)
        n=len(s)
        mini=float('inf')
        for i in count.values():
            if i==n//4:
                c+=1
        if c==4:
            return 0
        for right in range(len(s)):
            count[s[right]]-=1
            #print(count)
            while count['Q'] <= n/4 and count['W'] <= n/4 and count['E'] <= n/4 and count['R'] <=n/4:
                print(count, right, s[right], n/4)
                mini=min(mini, right-left+1)
                count[s[left]]+=1
                left+=1
            
        return mini
        
