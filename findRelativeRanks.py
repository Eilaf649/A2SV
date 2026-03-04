class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        k={}
        w= sorted(score, reverse=True)
        for i in range(len(w)):
            if i==0:
                k[w[0]]= "Gold Medal"
            elif i==1:
                k[w[1]]= "Silver Medal"
            elif i==2:
                k[w[2]]="Bronze Medal"
            else:
                k[w[i]]=str(i+1)
        x=[]
        for u in score:
            y=k.get(u)
            x.append(y)
        return x
    
            
        
