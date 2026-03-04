class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        x=[]
        c=Counter(s)
        for v in c.values():
            x.append(v)
        x.sort(reverse=True)
        f=""
        for i in range(len(x)):
            for key, val in c.items():
                if val==x[i] and key not in f:
                    for j in range(val):
                        f+=(key)
        return f
