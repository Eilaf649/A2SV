class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        x=[]
        count=Counter(arr1)
        diff=[]
        for i in arr1:
            if i not in arr2:
                diff.append(i)
        diff.sort()
        f=[]
        for x in arr2:
            for i in range(count[x]):
                    f.append(x)
        r=f+diff
        return r
        
