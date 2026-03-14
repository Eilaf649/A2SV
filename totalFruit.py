class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left=0
        window_size=0
        maxi=0
        adict=Counter()
        for right in range(len(fruits)):
            adict[fruits[right]]+=1
            while len(adict)>2:
                adict[fruits[left]]-=1
                if adict[fruits[left]]==0:
                    del adict[fruits[left]]
                left+=1
            maxi=max(maxi, right-left+1)
        return maxi
            

        
