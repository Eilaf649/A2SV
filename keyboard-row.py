class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1=['q','w','e','r','t', 'y','u','i','o','p']
        row2=['a','s','d','f','g','h','j','k','l']
        row3=['z','x','c','v','b','n','m']
        result=[]
        for word in words:
            count1=0
            count2=0
            count3=0
            for ch1 in word:
                ch=ch1.lower()
                if ch in row1:
                    count1+=1
                elif ch in row2:
                    count2+=1
                elif ch in row3:
                    count3+=1
            if count1==len(word) or count2==len(word) or count3==len(word):
                result.append(word)
        return result
                    
                
