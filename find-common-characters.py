class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res=[]
        shared_count= collections.Counter(words[0])
        for i in range(len(words)):
            char_counts= collections.Counter(words[i])
            for ch in shared_count.keys():
                shared_count[ch]= min(char_counts[ch], shared_count[ch],)        
        for char, counts in shared_count.items():
            for _ in range(counts):
                res.append(char)
        return res
            



