class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        left=0
        res=0
        adict=Counter()
        Counts=Counter(s1)
        for right in range(len(s2)):
            char=s2[right]
            adict[char]+=1

            #print(s2[left: right+1], res, left, right, adict)
            if adict==Counts:
                return True
            while right-left+1>len(s1) and left<len(s2):
                #print(s2[left: right+1], res, left, right, adict)
                #print(s2[left], s1, s2[left] in s1)
                adict[s2[left]]-=1
                if adict[s2[left]]==0:
                    del adict[s2[left]]
                #print(s2[left: right+1], res, left, right, adict)   
                if adict==Counts:
                    return True
                left+=1
        print(adict, left, right)
        
        if adict==Counts:
            return True
        else:
            return False
