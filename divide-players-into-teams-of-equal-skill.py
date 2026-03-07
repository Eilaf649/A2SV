class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        i=0
        j=len(skill)-1
        su= skill[i]+skill[j]
        chemistry=0
        while j>=i:
            if skill[i]+skill[j]!=su:
                return -1
            else:
                chemistry+= skill[i]*skill[j]
                i+=1
                j-=1
        return chemistry
        
