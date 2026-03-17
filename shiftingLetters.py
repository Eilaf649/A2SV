class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        res=""
        pref= [0]*(len(s)+1)
        for i in range(len(shifts)):
            left=shifts[i][0]
            right=shifts[i][1]
            direc=shifts[i][2]
            if direc==1:
                pref[left]+=1
                pref[right+1]-=1
            else:
                pref[left]-=1
                pref[right+1]+=1
        for k in range(1,len(pref)):
            pref[k]+=pref[k-1]
        for a in range(len(s)):
            res+=chr(((ord(s[a])-ord('a')+pref[a])%26)+ord('a'))
        print(res)
        return res
        
        
