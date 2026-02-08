class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        trans={}
        x=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
        "..-","...-",".--","-..-","-.--","--.."]
        letters=["a", "b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        res=[]
        all=[]
        for word in words:
            m=""
            for char in word:
                m+=x[letters.index(char)]
            all.append(m)
        for word in all:
            if word not in res:
                res.append(word)
        return(len(res))
