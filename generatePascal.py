class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans=[]
        if numRows==1:
            return [[1]]
        for i in range(numRows):
            ans.append([1]*(i+1))
        for j in range(2,len(ans)):
            for k in range(1,j):
                #print(j, k)
                ans[j][k]=ans[j-1][k]+ans[j-1][k-1]
        return (ans)
